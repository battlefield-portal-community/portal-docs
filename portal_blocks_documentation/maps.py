if True:
    import os

    os.environ["LOGURU_LEVEL"] = os.getenv("LOGURU_LEVEL", "INFO")

import json
import re
from timeit import default_timer as timer

# from loguru import logger

MAPS_LAYOUT_IMGS_DIR = "../docs/portal-builder/maps/images/layouts/"
MAPS_LAYOUT_IMGS_DIR_MD = "../images/layouts/"
MAPS_LAYOUT_FILE_EXT = "png"
MAPS_THUMBNAIL_FILE_EXT = "jpg"
MAPS_THUMBNAIL_IMGS_DIR_MD = "../images/thumbnails/"
MAPS_JSON_FILE = "./maps-and-modes.json"
MAPS_DOC_FILE = "_index.md"
MAPS_DOC_FILE_DIR = "../docs/portal-builder/maps/"


def identify(text: str):
    return re.sub(r"[^0-9A-Za-z]", "", text).lower()


def generate_text():
    timer_start = timer()
    print("Read map and mode information...")
    jsonFile = open(MAPS_JSON_FILE)
    mapsAndModes = json.load(jsonFile)
    print("Building map layout docs...")
    docLines = [
        "---\n",
        "title: Map Layouts\n",
        "---\n\n",
        "{{< toc-tree >}}\n\n",
    ]
    docFile = open(f"{MAPS_DOC_FILE_DIR}{MAPS_DOC_FILE}", mode="w+", encoding="utf-8")
    docFile.writelines(docLines)
    docFile.close()
    docLines.clear()
    for map in mapsAndModes["maps"]:
        docLines = ["---\n", f"title: {map}\n", "---\n\n", "{{< toc >}}\n\n"]
        docLines.append(f"# {map}\n\n")
        docLines.append(
            f"![{map} thumbnail]({MAPS_THUMBNAIL_IMGS_DIR_MD}{identify(map)}_thumbnail.{MAPS_THUMBNAIL_FILE_EXT})\n\n"
        )
        for modeType in mapsAndModes["modes"]:
            # docLines.append(f'{{{{< expand label="{modeType.capitalize()} Game Modes">}}}}\n')
            for mode in mapsAndModes["modes"][modeType]:
                docLines.append(f"## {map} - {mode} ({modeType})\n\n")
                docLines.append(f'{{{{< tabs "{map}-{mode}-{modeType}" >}}}}\n')
                for size in mapsAndModes["sizes"]:
                    docLines.append(f'{{{{< tab "{size}" >}}}}\n')
                    docLines.append(f"### {map} - {mode} ({modeType}) - {size}\n\n")
                    layoutId = f"{identify(map)}_{modeType}_{identify(mode)}_{size}"
                    layoutFilePath = (
                        f"{MAPS_LAYOUT_IMGS_DIR}{layoutId}.{MAPS_LAYOUT_FILE_EXT}"
                    )
                    print(f"{layoutId} = {map} - {modeType} - {mode} - {size}")
                    if os.path.exists(layoutFilePath):
                        print(
                            f"Map Layout of {map} - {modeType} - {mode} - {size} is supported!"
                        )
                        docLines.append(
                            f"![Map Layout of {map} - {modeType} - {mode} - {size}]({MAPS_LAYOUT_IMGS_DIR_MD}{layoutId}.{MAPS_LAYOUT_FILE_EXT})"
                        )
                    else:
                        print(
                            f"Map Layout of {map} - {modeType} - {mode} - {size} is not supported in portal or not yet documented!"
                        )
                        docLines.append(
                            "_Map Layout is not supported in portal or not yet documented by the community!_\n"
                        )
                    docLines.append("{{< /tab >}}\n")
                docLines.append("{{< /tabs >}}\n")
            # docLines.append(f'{{{{< /expand >}}}}\n')
        docFile = open(f"{MAPS_DOC_FILE_DIR}{identify(map)}.md", mode="w+", encoding="utf-8")
        docFile.writelines(docLines)
        docFile.close()
        docLines.clear()
    print(f"Finished building map layout docs in {timer() - timer_start} seconds")


generate_text()

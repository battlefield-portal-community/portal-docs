import json
from pathlib import Path
from timeit import default_timer as timer
from loguru import logger

from generators.utils import PROJECT_ROOT, identify, skip_function_if_env

MAPS_DOCS_DIR = PROJECT_ROOT / "docs" / "portal-builder" / "maps"
MAPS_LAYOUT_IMAGES_DIR = MAPS_DOCS_DIR / "images" / "layouts"
MAPS_LAYOUT_IMAGES_DIR_MD = "../images/layouts/"
MAPS_LAYOUT_FILE_EXT = "png"
MAPS_JSON_FILE = Path(__file__).parent / "maps-and-modes.json"


logger.debug("Read map and mode information...")
MAPS_AND_MODES = json.load(MAPS_JSON_FILE.open())
logger.debug("Successfully read map and mode information.")


def get_thumbnail_image(map_name: str) -> str:
    image_name = f"{identify(map_name)}_thumbnail.jpg"
    image_path = f"../images/thumbnails/{image_name}"
    return f"![{map_name} thumbnail]({image_path})"


def ensure_maps_dir_index():
    logger.debug("Generate Maps index...")
    header = [
        "---",
        "title: Map Layouts",
        "geekdocCollapseSection: true",
        "---\n",
        "{{< toc-tree >}}\n",
    ]
    (MAPS_DOCS_DIR / "_index.md").write_text('\n'.join(header))

    logger.debug("Successfully generated maps index.")


def generate_map_layout_doc(map_name: str):
    logger.debug(f"Generate doc for {map_name}...")
    docLines = [
        "---",
        f"title: {map_name}",
        "---",

        "{{< toc >}}",

        f"# {map_name}",
        get_thumbnail_image(map_name),
    ]

    for modeType, modes in MAPS_AND_MODES["modes"].items():
        for mode in sorted(modes):
            docLines.append(
                f"## {map_name} - {mode} ({modeType})"
            )
            docLines.append(
                f'{{{{< tabs "{map_name}-{mode}-{modeType}" >}}}}'
            )

            for size in (["standard"] if modeType == "core" else MAPS_AND_MODES["sizes"]):
                docLines.append(
                    f'{{{{< tab "{size}" >}}}}'
                )
                docLines.append(
                    f"### {map_name} - {mode} ({modeType}) - {size}"
                )
                layout_id = f"{identify(map_name)}_{identify(mode)}_{modeType}_{size}"
                layout_file_path = (MAPS_LAYOUT_IMAGES_DIR / layout_id).with_suffix(f".{MAPS_LAYOUT_FILE_EXT}")
                if layout_file_path.exists():
                    logger.debug(
                        f"Map Layout of {layout_id} is supported!"
                    )
                    layout_image_md = [
                        f"![Map Layout of {map_name} - {modeType} - {mode} - {size}]",
                        f"({MAPS_LAYOUT_IMAGES_DIR_MD}{layout_id}.{MAPS_LAYOUT_FILE_EXT})"
                    ]
                    docLines.append(''.join(layout_image_md))
                else:
                    logger.debug(
                        f"Map Layout of {layout_id} not found!"
                    )
                    docLines.append(
                        "_Map Layout is not supported in portal or not yet documented by the community!_"
                    )
                docLines.append("{{< /tab >}}")
            docLines.append("{{< /tabs >}}")

    map_md_file = MAPS_DOCS_DIR / f"{identify(map_name)}.md"
    map_md_file.write_text('\n'.join(docLines))

    logger.debug(f"Successfully generated doc for {map_name}.")


@skip_function_if_env("SKIP_GEN_MAP_LAYOUTS")
def generate():
    timer_start = timer()
    logger.info("Building map layout docs...")
    ensure_maps_dir_index()

    for map_name in sorted(MAPS_AND_MODES["maps"]):
        generate_map_layout_doc(map_name)

    logger.info(f"Finished building map layout docs in {timer() - timer_start} seconds")

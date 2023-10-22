if True:
    import os
    os.environ["LOGURU_LEVEL"] = os.getenv("LOGURU_LEVEL", "INFO")

import json
import pathlib
import shutil
from timeit import default_timer as timer

from loguru import logger

MAPS_LAYOUT_IMGS_DIR = "../docs/portal-builder/maps/images/layouts"
MAPS_JSON_FILE = "./maps-and-modes.json"

def generate_text():
    timer_start = timer()
    logger.info("Starting to build map layout docs")
    with open(MAPS_JSON_FILE) as JSON_FILE:
        mapsAndModes = json.loads(JSON_FILE.read())
    print(mapsAndModes)
    for map in mapsAndModes["maps"]:
        for mode in mapsAndModes["modes"]:
            for size in mapsAndModes["sizes"]:
                logger.debug(f"Built docs for {map} - {mode} - {size}")
    logger.info(f"Finished building map layout docs in {timer() - timer_start} seconds")

generate_text()
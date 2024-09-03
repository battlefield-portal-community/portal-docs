import re
import json
from typing import TYPE_CHECKING

import grequests
from loguru import logger

from generators.utils import skip_function_if_env
from .save_translations import save_translations_json
from . import config

if TYPE_CHECKING:
    import requests


@skip_function_if_env("SKIP_RAW_DOCS")
def gen_data():
    print("::group::Generate Raw Docs")
    save_translations_json()
    with open(config.DATA_DIR / "enabled_blocks.json") as file:
        blocks = json.load(file)["blocks"]
    with open(config.DATA_DIR / "rules_editor_version") as file:
        ver = json.load(file)

    logger.info(f"Got {len(blocks)} blocks, current portal Version {ver}")

    raw_docs_url = [
        f"https://portal.battlefield.com/{ver}/assets/help/{block}.md"
        for block in blocks
    ]
    logger.info(f"Getting raw docs for {len(blocks)} blocks....")
    rs = grequests.map((grequests.get(url) for url in raw_docs_url))
    logger.debug("Done..")
    invalid_blocks = []
    logger.info("Saving Raw Blocks")
    raw_docs_dir = config.DATA_DIR / "raw_docs"
    logger.debug(f"Deleting currently present raw docs, {len(list(raw_docs_dir.glob('*')))} files")
    for file in raw_docs_dir.glob("*"):
        logger.trace(f"Deleting {file}")
        file.unlink()

    req: 'requests.Response'
    for req, block in zip(rs, blocks):
        text: str
        text = req.text.strip()

        line_with_id = text.split('\n', 1)[0].strip()
        logger.trace(f"{block} has the ID {line_with_id}")
        is_block_valid = True
        block_docs_id = None
        if not text.startswith("<!DOCTYPE html>"):
            if regex_search_result := re.search(r"#+\s*%{(.*?)}", line_with_id):
                block_docs_id = regex_search_result.groups()[0]
        else:
            is_block_valid = False
            invalid_blocks.append(block)

        if block_docs_id is None:
            logger.trace(f"{block} has no ID")
        raw_doc_filename = f"{block}{'-' + block_docs_id if block_docs_id else ''}.md"
        with open(raw_docs_dir / raw_doc_filename, "w") as file:
            if is_block_valid:
                file.write(text)
            else:
                file.write("")

    logger.debug(f"{invalid_blocks} returned html")

    if invalid_blocks:
        with open(config.DATA_DIR / "invalid_blocks.json", "w") as file:
            json.dump(invalid_blocks, file, indent=4)

    logger.info("Done")
    print("::endgroup::")


if __name__ == "__main__":
    gen_data()

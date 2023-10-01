import re
import json
from typing import TYPE_CHECKING

import grequests
from loguru import logger

from .helper import project_dir, skip_function_if_env
from .save_translations import save_translations_json

if TYPE_CHECKING:
    import requests

@skip_function_if_env("SKIP_RAW_DOCS")
def gen_data():
    save_translations_json()
    with open(project_dir / "data" / "enabled_blocks.json") as file:
        blocks = json.load(file)["blocks"]
    with open(project_dir / "data" / "rules_editor_version") as file:
        ver = json.load(file)

    logger.debug(f"Got {len(blocks)} blocks, current portal Version {ver}")

    raw_docs_url = [
        f"https://portal.battlefield.com/{ver}/assets/help/{block}.md"
        for block in blocks
    ]
    logger.debug(f"Getting raw docs for {len(blocks)} blocks....")
    rs = grequests.map((grequests.get(url) for url in raw_docs_url))
    logger.debug("Done..")
    invalid_blocks = []
    logger.debug("Saving Raw Blocks")
    raw_docs_dir = project_dir / "data" / "raw_docs"
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
        raw_doc_filename = f"{block}{'-'+block_docs_id if block_docs_id else ''}.md"
        with open(raw_docs_dir / raw_doc_filename, "w") as file:
            if is_block_valid:
                file.write(text)
            else:
                file.write("")

    logger.debug(f"{invalid_blocks} returned html")

    if invalid_blocks:
        with open(project_dir / "data" / "invalid_blocks.json", "w") as file:
            json.dump(invalid_blocks, file, indent=4)

    logger.debug("Done")


if __name__ == "__main__":
    gen_data()

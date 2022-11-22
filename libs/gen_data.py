import json

import grequests

from loguru import logger

from helper import project_dir
from save_translations import save_translations_json


def gen_data():
    save_translations_json()
    with open(project_dir / "data" / "enabled_blocks.json") as file:
        blocks = json.load(file)['blocks']
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
    for file in raw_docs_dir.glob('*'):
        file.unlink()

    for req, block in zip(rs, blocks):
        with open(raw_docs_dir / f"{block}.md", 'w') as file:
            text = req.text
            if "<!DOCTYPE html>" not in text[0:20]:
                file.write(text)
            else:
                invalid_blocks.append(block)
    if len(invalid_blocks):
        logger.debug(f"{invalid_blocks} returned html")
    logger.debug("Done")


if __name__ == '__main__':
    gen_data()

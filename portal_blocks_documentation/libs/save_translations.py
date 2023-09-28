import json

import requests
from helper import project_dir
from loguru import logger


def save_translations_json(indent: int = 4):
    logger.debug("Saving Translations")
    with open(project_dir / "data" / "translations.json", "w") as file:
        json.dump(
            requests.get("https://api.gametools.network/bf2042/translations/").json(),
            file,
            indent=indent,
        )


if __name__ == "__main__":
    save_translations_json()

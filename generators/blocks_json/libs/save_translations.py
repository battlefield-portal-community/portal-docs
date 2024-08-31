import json

import requests

from deepdiff import DeepHash

from generators.utils import skip_function_if_env
from . import config
from loguru import logger

TRANSLATION_FILE = config.DATA_DIR / "translations.json"


@skip_function_if_env("SKIP_TRANSLATIONS")
def save_translations_json(indent: int = 4) -> bool:
    logger.debug("Saving Translations")
    upstream_json = requests.get("https://api.gametools.network/bf2042/translations/").json()
    local_json = json.load(open(TRANSLATION_FILE))
    if DeepHash(upstream_json)[upstream_json] == DeepHash(local_json)[local_json]:
        logger.info("No changes in translations")
        return False

    with open(TRANSLATION_FILE, "w") as f:
        json.dump(upstream_json, f, indent=indent)
    return True


if __name__ == "__main__":
    save_translations_json()

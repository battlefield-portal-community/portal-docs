import json
import operator
import re
from typing import Optional, TypedDict

import box
from box import Box
from loguru import logger

from .helper import project_dir, skip_function_if_env


class CleanDoc(TypedDict):
    block: str
    summary: str
    inputs: Optional[list]
    output: Optional[list]
    block_id: Optional[str]


i18n = None
mapped_translations = dict()


def populate_i18n():
    global i18n
    i18n = Box.from_json(filename=project_dir / "data" / "i18n.json")


def get_nested_dot(dot_string) -> str:
    try:
        return operator.attrgetter(dot_string)(i18n)
    except box.BoxKeyError:
        if block := mapped_translations.get(dot_string, False):
            return block
        raise


def gen_text(doc: str, rule_block: bool = False) -> str:
    if key := re.search(r"^#+\s*%{(.*?)}$", doc):
        mkey = key.groups()[0]
        if r := mapped_translations.get(mkey, False):
            replace_with = r
        else:
            replace_with = get_nested_dot(mkey)
        if rule_block:
            doc = doc.replace(key.group(), f"**{replace_with}**")
        else:
            doc = doc.replace(key.group(), f"{replace_with}")

    elif key := re.search(r"\*\*%{(.*?)}\*\*", doc):
        doc = doc.replace(key.group(), f"**{get_nested_dot(key.groups()[0])}**")
    elif key := re.search(r"^%{(.*?)}", doc):
        doc = doc.replace(key.group(), get_nested_dot(key.groups()[0]))
    elif key := re.search(r"%{(.*?)}", doc):
        doc = doc.replace(key.group(), f"**{get_nested_dot(key.groups()[0])}**")
    else:
        return doc
    return gen_text(doc)


# logger.debug("Get Translations from gametools")
# translations = requests.get("https://api.gametools.network/bf2042/translations/").json()['localizedTexts']


@skip_function_if_env("SKIP_GEN_DOCS_JSON")
def gen_json():
    populate_i18n()

    with open(project_dir / "data" / "translations.json") as file:
        translations = json.load(file)["localizedTexts"]

    logger.debug("Generate Mapping")
    for item in translations:
        mapped_translations[item["sid"]] = item["localizedText"]

    logger.info("Generate Docs")
    clean_names = []

    # delete all present docs before making new docs
    logger.info("Deleting currently present docs")
    for file in (project_dir / "docs_json").glob("*.json"):
        file.unlink()

    for raw_doc in sorted((project_dir / "data" / "raw_docs").glob("*.md")):
        bad_blocks = [
            "control_if"
            "controls_if_else",
            "missingActionBlockType_v1",
            "missingValueBlockType_v1",
        ]
        raw_doc_name_parts = raw_doc.stem.split("-")
        if len(raw_doc_name_parts) == 1:
            # continue because we only care for blocks with ID
            continue
        raw_doc_name_without_id = raw_doc_name_parts[0]
        block_id = raw_doc_name_parts[1]
        with open(raw_doc) as file:
            data = [
                key
                for key in re.sub("```.*```", "", file.read().strip(), flags=re.DOTALL)
                .strip()
                .split("\n")
                if key != ""
            ]
            if not len(data):
                continue

        if raw_doc_name_without_id == "ruleBlock":
            clean = [gen_text(data[0])]
            for index, line in enumerate(data[1:]):
                if index == 0:
                    clean.append(gen_text(line, rule_block=True).split("\n")[0])
                else:
                    clean.append(gen_text(line, rule_block=True))
        else:
            clean = [gen_text(line) for line in data]

        i = False
        o = False
        if "Inputs" in clean:
            i = clean.index("Inputs")
        if "Output" in clean:
            o = clean.index("Output")

        clean_doc: CleanDoc = dict()
        clean_doc['block_id'] = block_id
        if raw_doc_name_without_id == "subroutineInstanceBlock":
            clean_doc["block"] = "subroutineInstanceBlock"
        else:
            clean_doc["block"] = clean[0]

        clean_doc["summary"] = "\n".join(clean[1 : (i if i else o if o else None)])
        if i:
            clean_doc["inputs"] = clean[i + 1 : (o if o else None)]
        if o:
            clean_doc["output"] = clean[o + 1 :]

        k = f"ID_ARRIVAL_BLOCK_{raw_doc_name_without_id.upper()}"
        clean_name = mapped_translations.get(k, False)
        if not clean_name:
            if raw_doc_name_without_id == "controls_if_if":
                clean_name = "If"
            else:
                clean_name = clean_doc["block"].replace(" ", "").replace("#", "")
        elif clean_name == "VehicleTypes":
            clean_name = "VehicleTypesItem"

        if clean_name in ["RULE", "MOD", "CONDITION"]:
            clean_name = clean_name.capitalize()
        with open(project_dir / "docs_json" / f"{clean_name}.json", "w") as file:
            json.dump(clean_doc, file)
        clean_names.append(clean_name)
        logger.debug(f"{raw_doc_name_without_id} -> {clean_name}")

    with open(project_dir / "data" / "clean_names", "w") as file:
        json.dump(clean_names, file)
    logger.info("Gen docs complete")


if __name__ == "__main__":
    gen_json()

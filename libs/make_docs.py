import json
import requests
import re
from typing import TypedDict, Optional
from loguru import logger

from libs.helper import project_dir


class CleanDoc(TypedDict):
    block: str
    summary: str
    inputs: Optional[list]
    output: Optional[list]


def gen_text(doc: str) -> str:
    if key := re.search('#+\s*%{(.*?)}', doc):
        doc = doc.replace(key.group(), f'{mapped_translations[key.groups()[0]]}')
    elif key := re.search('\*\*%{(.*?)}\*\*', doc):
        doc = doc.replace(key.group(), f'**{mapped_translations[key.groups()[0]]}**')
    elif key := re.search('^%{(.*?)}', doc):
        mkey = key.groups()[0]
        doc = doc.replace(key.group(), f'{mapped_translations[mkey]}')
    elif key := re.search('%{(.*?)}', doc):
        mkey = key.groups()[0]
        doc = doc.replace(key.group(), f'**{mapped_translations[mkey]}**')
    else:
        return doc
    return gen_text(doc)


logger.debug("Get Translations from gametools")
translations = requests.get("https://api.gametools.network/bf2042/translations/").json()['localizedTexts']

# with open(project_dir / "data" / "translations.json") as file:
#     translations = json.load(file)['localizedTexts']

mapped_translations = dict()

logger.debug("Generate Mapping")
for item in translations:
    mapped_translations[item['sid']] = item['localizedText']


logger.debug("Generate Docs")
for raw_doc in sorted((project_dir / "data" / "raw_docs").glob("*.md")):
    logger.debug(f"Gen doc for {raw_doc.stem}")
    bad_blocks = ['controls_if_else', 'missingActionBlockType_v1', 'missingValueBlockType_v1']
    if raw_doc.stem in ['ruleBlock', 'subroutineBlock', 'subroutineInstanceBlock']:
        continue
    with open(raw_doc) as file:
        data = [
            key
            for key in re.sub('```.*```', '', file.read().strip(), flags=re.DOTALL).strip().split("\n") if key != ''
        ]
        if not len(data):
            continue
    clean = [gen_text(line) for line in data]
    clean_doc: CleanDoc = dict()
    clean_doc['block'] = clean[0]
    clean_doc['summary'] = clean[1]
    i = False
    o = False
    if 'Inputs' in clean:
        i = clean.index('Inputs')
    if 'Output' in clean:
        o = clean.index('Output')
    if i:
        clean_doc['inputs'] = clean[i+1:(o if o else None)]
    if o:
        clean_doc['output'] = clean[o+1:]

    k = f"ID_ARRIVAL_BLOCK_{raw_doc.stem.upper()}"
    clean_name = mapped_translations.get(k, False)
    if not clean_name:
        if raw_doc.stem == "controls_if_if":
            clean_name = "Control_If"
        else:
            clean_name = clean_doc['block'].replace(' ', '')

    with open(project_dir / "docs" / f'{clean_name}.json', 'w') as file:
        json.dump(clean_doc, file)

logger.debug("Gen docs complete")

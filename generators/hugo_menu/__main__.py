import json

from loguru import logger

from generators.utils import PROJECT_ROOT, PROJECT_DIR, identify, skip_function_if_env

MENU_FILE = PROJECT_ROOT / "hugo" / "data" / "menu" / "main.yaml"


def cleanup_menu_entries(sub_lookup_start: str, sub_lookup_end: str):
    if MENU_FILE.exists():
        startIndex = -1
        endIndex = -1
        entries = MENU_FILE.read_text().split("\n")
        for index, entry in enumerate(entries):
            if sub_lookup_start in entry:
                startIndex = index
            if sub_lookup_end in entry:
                endIndex = index
            if startIndex > -1 and endIndex > -1:
                break
        if endIndex - startIndex > 1:
            for i in range(startIndex, endIndex-1):
                deletedEntry = entries.pop(startIndex + 1)
                logger.debug(f"deleted entry from menu: {deletedEntry}")
        else:
            logger.debug(
                f"No menu entries to be cleaned up in defined section (start: {startIndex}, end: {endIndex}"
            )
        MENU_FILE.write_text("\n".join(entries))


def insert_menu_entry(menu_entry_name: str, menu_entry_ref: str, insert_before_lookup: str):
    if MENU_FILE.exists():
        entries = MENU_FILE.read_text().split("\n")
        for index, entry in enumerate(entries):
            if insert_before_lookup in entry:
                entries.insert(index, entry.split("#")[0] + menu_entry_ref)
                entries.insert(index, entry.split("#")[0] + menu_entry_name)
                break
        MENU_FILE.write_text("\n".join(entries))


def generate_entry_for_blocks():
    from generators.blocks_json.libs.config import DOCS_JSON_DIR
    for file in sorted(
            DOCS_JSON_DIR.glob("*.json"),
            key=lambda path: path.stem.lower()
    ):
        block_name = file.stem

        insert_menu_entry(
            f"- name: {block_name}",
            f'  ref: "/portal-builder/rules-editor/block-reference/{block_name}"',
            "# - name: generated-block-reference-end-do-not-remove"
        )


def generate_entry_for_maps():
    MAPS_JSON_FILE = PROJECT_DIR / "map_layouts" / "maps-and-modes.json"
    for map_name in sorted(json.loads(MAPS_JSON_FILE.read_text())["maps"]):
        insert_menu_entry(
            f"- name: {map_name}",
            f'  ref: "/portal-builder/maps/{identify(map_name)}"',
            "# - name: generated-map-reference-end-do-not-remove"
        )


@skip_function_if_env("SKIP_HUGO_MENU_GENERATION")
def generate():

    cleanup_menu_entries(
        sub_lookup_start="# - name: generated-block-reference-start-do-not-remove",
        sub_lookup_end="# - name: generated-block-reference-end-do-not-remove",
    )
    cleanup_menu_entries(
        sub_lookup_start="# - name: generated-map-reference-start-do-not-remove",
        sub_lookup_end="# - name: generated-map-reference-end-do-not-remove",
    )

    generate_entry_for_blocks()
    generate_entry_for_maps()

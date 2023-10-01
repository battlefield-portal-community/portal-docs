import json

from .libs.helper import CleanDoc, project_dir, project_root
from loguru import logger


def generate_docs():

    build_dir = project_root / "docs" / "portal_blocks"
    blocks_dir = build_dir / "blocks"

    build_dir.mkdir(exist_ok=True, parents=True)
    blocks_dir.mkdir(exist_ok=True)

    # delete all files if dir exists
    for f in blocks_dir.iterdir():
        if f.is_dir():
            (f / "official.md").unlink()


    # geekdocFilePath: portal_blocks/blocks/{file.stem}.md

    for file in (project_dir / "docs_json").glob("*.json"):
        with file.open("r") as JSON_FILE:
            doc_header = [
                "---",
                f"title: {file.stem}",
                "draft: false",
                "geekdocFilePath: false",
                "---",
            ]
            doc = ['\n'.join(doc_header)]

            doc_json: CleanDoc = json.loads(JSON_FILE.read())
            # doc.append(f"# {doc_json['block']}")
            doc.append(f"{doc_json['summary']}")
            if doc_json.get("inputs", False):
                doc.append("### Inputs")
                doc.append("\n".join(doc_json["inputs"]))
            if doc_json.get("output", False):
                doc.append("### Output")
                doc.append("\n".join(doc_json["output"]))
            doc.append(
                f"\n![{file.stem}](https://raw.githubusercontent.com/battlefield-portal-community/Image-CDN/main/portal_blocks/{file.stem}.png)"  # noqa
            )

            doc_dir = blocks_dir / f"{file.stem}"
            doc_dir.mkdir(exist_ok=True)

            doc_file = doc_dir / "official.md"
            doc_file.write_text("\n".join(doc))

            # add comment to tell where to write extra doc
            extra_doc = doc_dir / "extra.md"
            if not extra_doc.exists():
                extra_doc.write_text(f"<!-- Add extra documentation for {file.stem} in this file -->")
            logger.info(f"build {file.stem}")

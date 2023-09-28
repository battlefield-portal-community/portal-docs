import json

from .libs.helper import CleanDoc, project_dir, project_root
from loguru import logger

build_dir = project_root / "docs" / "portal_blocks"
blocks_dir = build_dir / "blocks"
extra_docs_dir = build_dir / "extra_docs"

build_dir.mkdir(exist_ok=True, parents=True)
blocks_dir.mkdir(exist_ok=True)
extra_docs_dir.mkdir(exist_ok=True)

# delete all files if dir exists
for file in build_dir.glob("*.md"):
    file.unlink()


for file in (project_dir / "docs_json").glob("*.json"):
    with file.open("r") as JSON_FILE, (blocks_dir / f"{file.stem}.md").open(
        "w"
    ) as DOC_FILE:
        doc = [
            f"""---
title: "{file.stem}"
draft: false
---"""
        ]
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
        if (extra_doc := extra_docs_dir / f"{file.stem}.md").exists():
            doc.append("## Extra Documentation")
            doc.append(extra_doc.read_text())

        DOC_FILE.write("\n".join(doc))
        logger.info(f"build {file.stem}")

import json
import shutil

from helper import project_dir
from helper import CleanDoc
from loguru import logger


build_base_dir = project_dir / "build"
build_dir = build_base_dir / "content" / "blocks"

# delete all files if dir exists
if build_dir.exists():
    shutil.rmtree(build_dir)


# recreate base structure
build_dir.mkdir(exist_ok=True, parents=True)

for file in (project_dir / "docs_json").glob("*.json"):
    with file.open('r') as JSON_FILE, (build_dir / (file.stem + ".md")).open('w') as DOC_FILE:
        doc = [
            f"""---
title: "{file.stem}"
draft: false
---"""
        ]
        doc_json: CleanDoc = json.loads(JSON_FILE.read())
        # doc.append(f"# {doc_json['block']}")
        doc.append(f"{doc_json['summary']}")
        if doc_json.get('inputs', False):
            doc.append("### Inputs")
            doc.append("\n".join(doc_json['inputs']))
        if doc_json.get('output', False):
            doc.append("### Output")
            doc.append("\n".join(doc_json['output']))
        doc.append(
            f"\n![{file.stem}](https://raw.githubusercontent.com/battlefield-portal-community/Image-CDN/main/portal_blocks/{file.stem}.png)"  # noqa
        )
        if extra := doc_json['extra']:
            doc.append("## Extra Documentation")
            doc.append(extra)

        DOC_FILE.write("\n".join(doc))
        logger.info(f"build {file.stem}")




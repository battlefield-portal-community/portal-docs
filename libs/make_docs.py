import json
import requests

from libs.helper import project_dir
blocks_file = project_dir / "data" / "enabled_blocks.json"
with blocks_file.open() as file:
    blocks = json.load(file)

for block in blocks['blocks']:
    print(f"{block}, {requests.get(f'https://portal.battlefield.com/2688699/assets/help/{block}.md')}")



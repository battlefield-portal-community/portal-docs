import pathlib
from typing import Optional, TypedDict

project_dir = pathlib.Path(__file__).parent.parent
project_root = project_dir.parent


class CleanDoc(TypedDict):
    block: str
    summary: str
    extra: str
    inputs: Optional[list]
    output: Optional[list]

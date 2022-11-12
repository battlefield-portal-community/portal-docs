import pathlib
from typing import TypedDict, Optional

project_dir = pathlib.Path(__file__).parents[1]


class CleanDoc(TypedDict):
    block: str
    summary: str
    extra: str
    inputs: Optional[list]
    output: Optional[list]

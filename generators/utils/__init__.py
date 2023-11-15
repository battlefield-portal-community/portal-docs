import functools
import os
import re
import pathlib
from typing import Optional, TypedDict, Callable
from loguru import logger

PROJECT_DIR = None
for directory in pathlib.Path(__file__).parents:
    if directory.name == "generators":
        PROJECT_DIR = directory

if PROJECT_DIR is None:
    raise ValueError("Unable to set PROJECT_DIR")

PROJECT_ROOT = PROJECT_DIR.parent


class CleanDoc(TypedDict):
    block: str
    summary: str
    inputs: Optional[list]
    output: Optional[list]


def skip_function_if_env(env_flag) -> Callable:
    def empty(*args, **kwargs):
        pass

    def wrapper(function: Callable):
        if os.getenv(env_flag, "False").lower() == "true":
            logger.debug(f"Skipping {function.__name__} as {env_flag} is set")
            return empty

        @functools.wraps(function)
        def inner(*args, **kwargs):
            return function(*args, **kwargs)

        return inner

    return wrapper


def identify(text: str):
    return re.sub(r"[^0-9A-Za-z]", "", text).lower()

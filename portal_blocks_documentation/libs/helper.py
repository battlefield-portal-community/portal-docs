import functools
import os
import pathlib
from typing import Optional, TypedDict, Callable
from loguru import logger

project_dir = pathlib.Path(__file__).parent.parent
project_root = project_dir.parent


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

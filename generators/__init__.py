import os
os.environ["LOGURU_LEVEL"] = os.getenv("LOGURU_LEVEL", "DEBUG")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

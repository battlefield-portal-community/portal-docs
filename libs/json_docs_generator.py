from dotenv import load_dotenv
from urllib3.exceptions import MaxRetryError
from loguru import logger
load_dotenv()

if __name__ == '__main__':
    from gen_data import gen_data  # order matters because of monkey patching
    from get_block_names import get_block_names

    try:
        print("::group::Get Block Names")
        get_block_names()
        print("::endgroup::")
        print("::group::Generate Raw Docs")
        gen_data()
        print("::endgroup::")
        print("::group::Generate Docs Json")
        from gen_docs_json import gen_json  # import later as i18n needs to be populated with the latest changes
        gen_json()
        print("::endgroup::")
    except MaxRetryError as why:
        logger.error(why)
        raise


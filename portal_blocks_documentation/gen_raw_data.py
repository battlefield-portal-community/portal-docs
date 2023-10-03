if True:
    from dotenv import load_dotenv

    load_dotenv()

from .libs.gen_data import gen_data  # order matters because of monkey patching
from .libs.gen_docs_json import gen_json
from .libs.get_block_names import get_block_names


def generate():
    try:
        print("::group::Get Block Names")
        get_block_names()
        print("::endgroup::")
        print("::group::Generate Raw Docs")
        gen_data()
        print("::endgroup::")
        print("::group::Generate Docs Json")
        gen_json()
        print("::endgroup::")
    except Exception as why:
        print(why)
        raise


if __name__ == '__main__':
    generate()

from .libs.gen_data import gen_data  # order matters because of monkey patching
from .libs.gen_docs_json import gen_json
from .libs.get_block_names import get_block_names


def generate():
    try:
        get_block_names()
        gen_data()
        gen_json()
    except Exception as why:
        print(why)
        raise


if __name__ == '__main__':
    generate()

from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    from gen_data import gen_data  # order matters because of monkey patching
    from get_block_names import get_block_names
    from gen_docs_json import gen_json

    print("::group::Get Block Names")
    get_block_names()
    print("::endgroup::")
    print("::group::Generate Raw Docs")
    gen_data()
    print("::endgroup::")
    print("::group::Generate Docs Json")
    gen_json()
    print("::endgroup::")

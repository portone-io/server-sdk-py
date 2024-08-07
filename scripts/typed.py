from pathlib import Path


def gen() -> None:
    root = Path(__file__).parent.parent.joinpath("./portone_server_sdk")
    for path in root.glob("**/"):
        with open(path.joinpath("./py.typed"), "wb") as f:
            f.write(b"\n")

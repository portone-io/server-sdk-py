import subprocess
from pathlib import Path

project_path = Path(__file__).resolve().parent.parent
patch_dir = project_path.joinpath("patches")
openapi_path = project_path.joinpath("portone_server_sdk/_openapi")


def save() -> None:
    subprocess.run(
        [
            "git",
            "format-patch",
            "--no-stat",
            "--minimal",
            "-N",
            "-o",
            patch_dir,
            "origin/openapi",
        ],
        cwd=openapi_path,
    )
    subprocess.run(
        [
            "git",
            "reset",
            "origin/openapi",
        ],
        cwd=openapi_path,
    )


def apply() -> None:
    subprocess.run(
        [
            "git",
            "am",
            "--abort",
        ],
        cwd=openapi_path,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    patches = [str(patch) for patch in patch_dir.glob("*.patch")]
    subprocess.run(
        ["git", "am", "--3way", *patches],
        cwd=openapi_path,
    )

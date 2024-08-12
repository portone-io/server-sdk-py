import subprocess
from pathlib import Path
from shutil import rmtree

project_path = Path(__file__).resolve().parent.parent
patch_dir = project_path.joinpath("patches")
openapi_path = project_path.joinpath("portone_server_sdk/_openapi")
generated_path = project_path.joinpath("openapi/generated")

TAG_NAME = "patch-base"


def clean() -> None:
    rmtree(openapi_path, False)


def save() -> None:
    subprocess.run(
        [
            "git",
            "format-patch",
            "--zero-commit",
            "--no-stat",
            "--minimal",
            "-N",
            "-o",
            patch_dir,
            TAG_NAME,
        ],
        cwd=openapi_path,
        check=True,
    )


def apply() -> None:
    openapi_path.mkdir()
    subprocess.run(["git", "init", openapi_path])
    subprocess.run(
        [
            "git",
            "config",
            "commit.gpgSign",
            "false",
        ],
        cwd=openapi_path,
        check=True,
    )
    subprocess.run(["git", "tag", TAG_NAME], cwd=project_path, check=True)
    subprocess.run(
        [
            "git",
            "filter-repo",
            "--force",
            "--subdirectory-filter",
            "openapi/generated",
            "--target",
            openapi_path,
        ],
        cwd=project_path,
        check=True,
    )
    subprocess.run(["git", "tag", "-d", TAG_NAME], cwd=project_path, check=True)
    subprocess.run(["git", "checkout", TAG_NAME], cwd=openapi_path, check=True)
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
    patches = sorted(str(patch) for patch in patch_dir.glob("*.patch"))
    if patches:
        subprocess.run(["git", "am", "--3way", *patches], cwd=openapi_path, check=True)

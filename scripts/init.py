import subprocess
from pathlib import Path


def run() -> None:
    project_dir = Path(__file__).parent.parent
    openapi_dir = project_dir.joinpath("portone_server_sdk/_openapi")

    subprocess.run(["pre-commit", "install"], cwd=project_dir)
    subprocess.run(["git", "config", "commit.gpgSign", "false"], cwd=openapi_dir)

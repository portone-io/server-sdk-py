import subprocess
from pathlib import Path


def run() -> None:
    project_dir = Path(__file__).parent.parent

    subprocess.run(["pre-commit", "install"], cwd=project_dir, check=True)

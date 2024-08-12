def gen() -> None:
    import subprocess
    import tomllib
    from pathlib import Path

    project_dir = Path(__file__).resolve().parent.parent
    generated_dir = project_dir.joinpath("portone_server_sdk/_generated")
    generated_dir.mkdir(parents=True, exist_ok=True)

    with open(project_dir.joinpath("pyproject.toml"), "rb") as file:
        pyproject = tomllib.load(file)
        version: str = pyproject["project"]["version"]

    commit_hash = subprocess.check_output(
        args=["git", "rev-parse", "HEAD"],
        cwd=project_dir,
        text=True,
    ).strip()

    with open(generated_dir.joinpath("_env.py"), "wt") as file:
        file.write(
            f'user_agent = "portone-io/server-sdk-py v{version} ({commit_hash})"\n'
        )

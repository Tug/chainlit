import os
import subprocess
import sys

env = os.environ.copy()
env["CI"] = "true"

workspace_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def build_frontend():
    try:
        subprocess.run(
            ["pnpm", "install", "--frozen-lockfile"],
            cwd=workspace_dir,
            check=True,
            env=env,
        )
        subprocess.run(
            ["pnpm", "run", "buildForPoetry"], cwd=workspace_dir, check=True, env=env
        )
    except subprocess.CalledProcessError:
        print("Error: Failed to build frontend.")
        sys.exit(1)
    except FileNotFoundError:
        print("Frontend folder not found.")
        sys.exit(1)


if __name__ == "__main__":
    build_frontend()

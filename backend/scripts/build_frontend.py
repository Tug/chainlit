import os
import subprocess
import sys

env = os.environ.copy()
env["CI"] = "true"

workspace_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def build_frontend():
    if os.path.exists(
        os.path.join(workspace_dir, "backend", "chainlit", "frontend", "dist")
    ):
        return
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
    except FileNotFoundError as fnfe:
        print(fnfe)
        print(f"pnpm or frontend folder not found in {workspace_dir}")
        sys.exit(1)


if __name__ == "__main__":
    build_frontend()

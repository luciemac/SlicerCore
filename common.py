# Baseline Slicer repository, change this when rebasing
GIT_URL = "https://github.com/AlexyPellegrini/Slicer.git"
GIT_REVISION = "2d798bde687300cbd0bb9f124aa24002fcb73baa"

# Directories used by the scripts
SLICER_DIR = "Slicer"
PATCH_DIR = "patch"

import subprocess
import os

def execute_process(cmd: str, cwd: str = ".") -> str:
    """Run a shell command and return the process standard output as a str.
    Throws an exception with subprocess stderr if return code is not zero.
    """
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running command: {cmd}\nError message:\n{e.stderr}\n")


def mkpath(file_path: str) -> None:
    """Create the directories tree for given file path"""
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)


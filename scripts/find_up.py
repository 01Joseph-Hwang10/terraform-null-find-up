import sys
import json
from os import listdir, getcwd
from os.path import dirname, join


def find_up(
    targets: list[str],
    cwd: str | None = None,
) -> str | None:
    """Find the target file or directory path in the parent directories"""
    if not cwd:
        cwd = getcwd()

    def do_find_up(targets: list[str], cwd: str) -> str | None:
        if cwd == dirname(cwd):
            return None
        for target in targets:
            if target in listdir(cwd):
                return join(cwd, target)
        return do_find_up(targets, dirname(cwd))

    return do_find_up(targets, cwd)


if __name__ == "__main__":
    payload: dict = json.loads(sys.stdin.read())
    targets = str(payload.get("targets")).split(",")
    cwd = payload.get("cwd")
    print(json.dumps({"path": find_up(targets, cwd)}))

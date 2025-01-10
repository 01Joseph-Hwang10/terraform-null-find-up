import sys
import json
from os import listdir, getcwd
from os.path import dirname, join


def find_up(
    targets: str | list[str],
    cwd: str | None = None,
) -> str | None:
    """Find the target file or directory path in the parent directories"""
    if not cwd:
        cwd = getcwd()

    def do_find_up(targets: list[str], cwd: str) -> str | None:
        if cwd == dirname(cwd):
            return None
        if targets in listdir(cwd):
            return join(cwd, targets)
        return do_find_up(targets, dirname(cwd))

    return do_find_up(targets if isinstance(targets, list) else targets, cwd)


if __name__ == "__main__":
    payload: dict = json.loads(sys.stdin.read())
    targets = payload.get("targets")
    cwd = payload.get("cwd")
    print(json.dumps({"path": find_up(targets, cwd)}))

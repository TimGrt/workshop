#!/usr/bin/env python3

import subprocess
import argparse

from typing import Any, Sequence


class CalledProcessError(RuntimeError):
    pass


def cmd_output(*cmd: str, retcode: int | None = 0, **kwargs: Any) -> str:
    kwargs.setdefault("stdout", subprocess.PIPE)
    kwargs.setdefault("stderr", subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def check_vault_files(files: Sequence[str]) -> int:
    staged_files = set(
        cmd_output("git", "diff", "--staged", "--name-only", *files).splitlines()
    )
    invalid_files = []

    required_line = "$ANSIBLE_VAULT;1.1;AES256"
    for file in staged_files:
        with open(file) as f:
            if f.readline().strip("\n") != required_line:
                invalid_files.append(file)
        f.close()

    if invalid_files:
        for file in sorted(invalid_files):
            print(f"Unencrypted file found: {file}")
        return 1
    else:
        return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    args = parser.parse_args(argv)

    return check_vault_files(args.files)


if __name__ == "__main__":
    raise SystemExit(main())

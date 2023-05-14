#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from typing import AbstractSet
from typing import Sequence

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output


def is_on_branch(protected: AbstractSet[str]) -> int:
    ref_name = cmd_output("git", "symbolic-ref", "HEAD")

    chunks = ref_name.strip().split("/")
    branch_name = "/".join(chunks[2:])

    if branch_name in protected:
        print(f"Commiting to {branch_name} branch is not allowed!")
        return 1
    else:
        return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("branches", nargs="+", help="branches to disallow commits to")
    args = parser.parse_args(argv)
    protected = frozenset(args.branches + ["master", "main"])

    return is_on_branch(protected)


if __name__ == "__main__":
    raise SystemExit(main())

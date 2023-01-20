import os
from pathlib import Path


def pre_archive_check(self):
    check_existing(self.stdin, self.stdout)


def check_existing(stdin: Path, stdout: Path):
    if stdin != stdout and not stdout.is_relative_to(stdin):
        return True
    else:
        raise Exception

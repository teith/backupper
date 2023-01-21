import os
from pathlib import Path
from datetime import datetime


def check_fs(stdin: Path, stdout: Path):
    check_existing(stdin, stdout)
    check_tree(stdin, stdout)


def check_existing(stdin: Path, stdout: Path):
    if os.path.isdir(stdin) and os.path.isdir(stdout):
        return
    else:
        raise Exception


def check_tree(stdin: Path, stdout: Path):
    if stdin != stdout and not stdout.is_relative_to(stdin):
        return
    else:
        raise Exception


def create_zip_dir(stdout: Path):
    backup_dir = os.path.join(
        'backupper_{date}'
    ).format(
        date=datetime.now().strftime("%Y-%m-%d_%H:%M")
    )
    zip_dir = os.path.join(stdout, backup_dir)
    os.makedirs(zip_dir, exist_ok=False)
    return zip_dir

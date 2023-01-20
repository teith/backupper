import os
from pathlib import Path
from archiver.tools.checking import pre_archive_check


class Archiver:
    stdin: Path = os.path.abspath('')
    stdout: Path = os.path.abspath('')
    size: int = 1073741824
    password: str = ''
    cloud_name: str = ''

    def __init__(self):
        self.create_archive()

    def create_archive(self):
        pre_archive_check(self)



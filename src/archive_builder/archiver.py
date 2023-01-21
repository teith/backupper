import os
from pathlib import Path
from archive_builder.fs_processor import check_fs, create_zip_dir
from archive_builder.zip_processor import create_zip


class Archiver:
    stdin: Path = os.path.abspath('')
    stdout: Path = os.path.abspath('')
    size: int = 1073741824
    password: str = ''
    zip_dir: Path = os.path.abspath('')

    def __init__(self, stdin, stdout, size, password):
        self.stdin = stdin
        self.stdout = stdout
        self.size = size
        self.password = password

    def create_archive(self):
        check_fs(self.stdin, self.stdout)
        self.zip_dir = create_zip_dir(self.stdout)
        create_zip(self)
        return self.zip_dir





# ...def backup(self, backup_target, save_path):
#     backup = self.archiver.create(backup_target)
#     self.provider.upload(backup, save_path)
#
#
# def view(request: Request, backuoer = Depends(get_backuper)):
#     backuper.backup(…)

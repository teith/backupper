import multiprocessing
from threading import Thread
from subprocess import Popen, PIPE
import os


class CreateZipThread(Thread):
    def __init__(self, command):
        self.stderr = None
        self.stdout = None
        self.command = command
        Thread.__init__(self)

    def run(self):
        p = Popen(
            self.command,
            shell=True,
            stdout=PIPE,
            stderr=PIPE
        )
        self.stdout, self.stderr = p.communicate()


def build_command(archiver):
    password = '-p' + archiver.password or None
    stdin = str(archiver.stdin)
    zip_archive = str(os.path.join(archiver.zip_dir, 'backup.zip'))
    size = '-v' + str(archiver.size) + 'm'
    mmt = '-mmt=' + str(multiprocessing.cpu_count())
    command = (' ').join(['7z', 'a', '-tzip', '-ssw', '-sfx',
               '-mm=Deflate64', mmt, size, password,
               '-mx6', '-r0', zip_archive, stdin])
    print(command)
    return command


def create_zip(archiver):
    command = build_command(archiver)
    archive = CreateZipThread(command)
    archive.start()
    archive.join()

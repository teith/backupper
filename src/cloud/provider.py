import os
from pathlib import Path


class Provider:
    cloud_name: str = ''
    login: str = ''
    password: str = ''
    output_path: Path = os.path.abspath('')

    def __init__(self, cloud_name, login, password, output_path):
        self.cloud_name = cloud_name
        self.login = login
        self.password = password
        self.output_path = output_path

    def check_fs(self, estimated_archive_size):
        return estimated_archive_size

    def upload(self, archive_path):
        return archive_path




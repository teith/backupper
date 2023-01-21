import os
from pathlib import Path
from archive_builder.archiver import Archiver
from cloud.provider import Provider


async def get_archiver(folder_stdin: Path = os.path.abspath(''),
                       folder_stdout: Path = os.path.abspath(''),
                       archive_size: int = 1073741824,
                       archive_password: str = 'password'):
    return Archiver(
        stdin=folder_stdin,
        stdout=folder_stdout,
        size=archive_size,
        password=archive_password
    )


async def get_provider(cloud_name: str = 'mail',
                       cloud_login: str = 'user',
                       cloud_password: str = 'password',
                       cloud_output_path: Path = os.path.abspath('')):
    return Provider(
        cloud_name=cloud_name,
        login=cloud_login,
        password=cloud_password,
        output_path=cloud_output_path
    )

from pydantic import BaseSettings
from typing import Dict, Any
from yaml import load, Loader
import os


def yaml_config_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    with open(os.path.join('configuration', 'config.yaml'), "r") as f:
        return load(f, Loader=Loader)


class Settings(BaseSettings):
    DB_HOST: str = None
    DB_PORT: int = 5432
    DB_USER: str = None
    DB_NAME: str = None
    DB_PASSWORD: str = None

    REDIS_HOST: str = None
    REDIS_PORT: int = 6379

    class Config:
        env_file_encoding = 'utf-8'

        @classmethod
        def customise_sources(
                cls,
                init_settings,
                env_settings,
                file_secret_settings,
        ):
            return (
                init_settings,
                yaml_config_settings_source,
                env_settings,
                file_secret_settings,
            )


def get_settings():
    return Settings()

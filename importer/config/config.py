"""App configuration"""
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    """App configuration"""

    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings() -> Settings:
    """Returns a Settings object with the app config"""
    return Settings()
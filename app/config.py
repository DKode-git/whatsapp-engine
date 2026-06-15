import os
import typing
import pydantic
import pathlib
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    USE_META_API: bool
    META_API_KEY: str

    PLAYWRIGHT_ENABLED: bool
    DAILY_LIMIT_PLAYWRIGHT: int

    MIN_DELAY_SECONDS: int
    MAX_DELAY_SECONDS: int

    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXP_SECONDS: int


settings = Settings()

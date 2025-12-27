from typing import List
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MONGODB_URI: str
    MONGODB_DB_NAME: str
    ALLOWED_ORIGINS: List[str]
    SESSION_EXPIRES_DAYS: int
    COOKIE_SECURE: bool = False # set to true on production
    SESSION_COOKIE_NAME: str = "session_token"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LOG_LEVEL: str = "DEBUG"
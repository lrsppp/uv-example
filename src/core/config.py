from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../../.env", extra="ignore")

    PROJECT_NAME: str
    DEBUG: bool
    DATABASE_URL: str


settings = Settings()

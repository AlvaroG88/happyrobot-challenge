from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./happyrobot.db"
    API_KEY: str = "hr-dev-key-2024"
    FMCSA_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Yugen Story Engine"
    database_url: str = "sqlite:///data/stories.db"
    openai_api_key: str = ""
    claude_api_key: str = ""
    log_level: str = "INFO"


settings = Settings()

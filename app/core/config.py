from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_env: str = "development"
    secret_key: str = "change_me"

    database_url: str = "postgresql+asyncpg://app_user:change_me@postgres:5432/app_db"
    redis_url: str = "redis://redis:6379/0"

    postgres_db: str = "app_db"
    postgres_user: str = "app_user"
    postgres_password: str = "change_me"

    # Set by deploy script or CI/CD
    last_deploy: str = "—"
    current_image: str = "local"
    git_sha: str = "local"
    nginx_status: str = "active"


settings = Settings()

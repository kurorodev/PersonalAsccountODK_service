from pydantic_settings import BaseSettings, SettingsConfigDict

from app.schemas.user_schema import UserCreateSchema


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        secrets_dir="/run/secrets",
        extra="allow",
        from_attributes=True,
    )

    db_url: str
    initial_user_schema: UserCreateSchema | None = None
    allow_origins: list[str]


settings = AppSettings(_env_file="dev.env")

from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_name: str = "FastAPI Shop"
    debug: bool = True
    database_url: str = f"sqlite:///{(BASE_DIR / 'shop.db').as_posix()}"
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    static_dir: str = str(BASE_DIR / "static")
    images_dir: str = str(BASE_DIR / "static" / "images")

    class Config:
        env_file = str(BASE_DIR / ".env")


settings = Settings()

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL = 'sqlite+aiosqlite:///./test.db'


settings = Settings()

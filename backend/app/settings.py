from pydantic import BaseSettings


class Settings(BaseSettings):
    PGHOST: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str
    PGPORT: int
    PGDATABASEURL: str

    class Config:
        env_file = '.env'


settings = Settings()

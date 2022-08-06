from os import environ

from pydantic import BaseSettings


class Config(BaseSettings):
    db_uri: str = environ["DATABASE_URI"]


Settings = Config()

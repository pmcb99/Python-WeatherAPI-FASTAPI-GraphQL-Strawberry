from os import environ, path
import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass

load_dotenv(find_dotenv())
@dataclass(frozen=True)
class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')

@dataclass(frozen=True)
class DevConfig(Config):
    DEBUG = True
    TESTING = True
    weather_api_key: str = os.getenv('weather_api_key')
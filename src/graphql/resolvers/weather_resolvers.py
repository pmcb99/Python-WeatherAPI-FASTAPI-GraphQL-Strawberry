from src.graphql.scalars.weather_scalar import WeatherData
from src.graphql.db.dict_based import weather_db, city_db
from typing import Dict
from src.api.weather_api import get_hourly_weather_by_city_and_date

def get_weather_data(city: str, date: str)->WeatherData:
    #Add to db
    get_hourly_weather_by_city_and_date(city,date)
    return weather_db[f'{city}|{date}']

def add_favourite_city_for_user(city: str, user: str)->str:
    city_db[user] = city
    return f"Added {city} to favourites for user {user}"

def get_favourite_city(user: str)->WeatherData:
    return city_db[str(user)] if str(user) in city_db else "NULL"
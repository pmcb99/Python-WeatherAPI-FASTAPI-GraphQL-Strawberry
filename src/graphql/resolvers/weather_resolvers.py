from src.graphql.scalars.weather_scalar import WeatherData
from src.graphql.db.dict_based import weather_db, city_db, user_db
from src.api.weather_api import get_hourly_weather_by_city_and_date

def get_weather_data(city: str, date: str)->WeatherData:
    result = get_hourly_weather_by_city_and_date(city, date)
    #Can remove if statement to return an empty WD object but would be less descriptive to end user
    if not result.times:
        raise ValueError("API returned no data. Check city and date values.")
    else:
        weather_db[f'{city}|{date}'] = result
    return result

def add_favourite_city_for_user(city: str, user: str)->str:
    if user in user_db:
        city_db[user] = city
        return f"Added {city} to favourites for user {user}"
    return f"User {user} does not exist"

def get_favourite_city(user: str)->WeatherData:
    return city_db[str(user)] if str(user) in city_db else "NULL"
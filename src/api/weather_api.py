import requests
from typing import Dict
from src.graphql.scalars.weather_scalar import WeatherData
from config.config import DevConfig

def get_hourly_weather_by_city_and_date(city: str, date: str) -> None:
    from src.graphql.db.dict_based import weather_db 
    #Check database for value using CITY|DATE as key and update db as required
    if '|'.join([city,date]) in weather_db:
        return weather_db['|'.join([city,date])]
    weather_api_url = f"http://api.weatherapi.com/v1/history.json?key={DevConfig.weather_api_key}&q={city}&dt={date}"
    r = requests.get(weather_api_url, headers={'Accept': 'application/json'})
    if r.status_code == 200:
        print(r.status_code)
        print(r.json())
        hourly_data = r.json()['forecast']['forecastday'][0]['hour']
        weather_data_object = WeatherData(date=date, city=city, times=[], temperatures=[], humidities=[])
        for hour in hourly_data:
            weather_data_object.times.append(hour['time'])
            weather_data_object.temperatures.append(hour['temp_f'])
            weather_data_object.humidities.append(hour['humidity'])
        weather_db[f'{city}|{date}'] = weather_data_object
        hourly_data = r.json()['forecast']['forecastday'][0]['hour']
        print(type(hourly_data))
    else:
        print(f"Status Code: {r.status_code}, Content: {r.json()}")
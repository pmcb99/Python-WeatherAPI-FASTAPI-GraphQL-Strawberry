import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from config.config import DevConfig
from typing import Dict, List
from src.graphql.resolvers.weather_resolvers import get_weather_data 
import json
import requests

'''
---IMPORTANT DEMO NOTES---
    ------------------
API limits historical data to 7 days
API uses date format YYYY-MM-DD

'''
#7pm -> Stopwatch at 3h
#8.04pm -> stopwatch at 4h

'''
1 query for weather where you input a city and date, output should be data on temp and humidity by time. Bonus: thoughtful about picking the data type for the output
1 mutation for saving your favorite
1 query for getting weather from your fav locations
'''

'''USING DICTIONARY-BASED DB TO STORE ALL DATA'''
db = {}
strawberry_db = {}
favourite_city_db = {}

def get_hourly_weather_by_city_and_date(city: str, date: str) -> Dict[str,str]:
    #Check database for value using CITY|DATE as key and update db as required
    if '|'.join([city,date]) in db:
        return strawberry_db['|'.join([city,date])]
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
        strawberry_db[f'{city}|{date}'] = weather_data_object
        hourly_data = r.json()['forecast']['forecastday'][0]['hour']
        print(type(hourly_data))
    else:
        print(f"Status Code: {r.status_code}, Content: {r.json()}")
    return r.json()

def get_temperatures_for_date(root)->"TemperatureAtTime":
    pass

@strawberry.type
class Mutation:
    @strawberry.mutation
    def addFavouriteCity(self, city: str, userName: str) -> str:
        favourite_city_db[userName] = city
        print(f"Added {city} to favourites for user {userName}")
        return f"Added {city} to favourites for user {userName}"

# @strawberry.type
# class Temperature:
#     date: str
#     time: str
#     temperature: float
    
# @strawberry.type
# class Humidity:
#     date: str
#     time: str
#     humidity: float

@strawberry.type
class WeatherData:
    date: str
    city: str
    times: List[str]
    temperatures: List[float]
    humidities: List[float]

# def get_weather_data(city: str, date: str)->WeatherData:
#     get_hourly_weather_by_city_and_date(city,date)
#     return strawberry_db[f'{city}|{date}']

@strawberry.type
class Query:
    @strawberry.field
    def getWeatherData(self, date: str, city: str) -> WeatherData:
        return get_weather_data(city,date,strawberry_db)
    @strawberry.field
    def getFavouriteCity(self,userName: str) -> str:
        return favourite_city_db[userName]

# get_hourly_weather_by_city_and_date('London', '2023-02-23') #insert into db
schema = strawberry.Schema(Query,mutation=Mutation)
graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
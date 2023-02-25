import strawberry
from src.graphql.resolvers.weather_resolvers import get_weather_data, get_favourite_city
from src.graphql.scalars.weather_scalar import WeatherData
from typing import Dict

@strawberry.type
class Query:
    @strawberry.field
    def getWeatherData(self, date: str, city: str) -> WeatherData:
        return get_weather_data(city,date)
    @strawberry.field
    def getFavouriteCity(self,userName: str) -> str:
        return get_favourite_city(userName)
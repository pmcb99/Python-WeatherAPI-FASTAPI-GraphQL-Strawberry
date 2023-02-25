import strawberry
from typing import Dict
from src.graphql.resolvers.weather_resolvers import add_favourite_city_for_user

@strawberry.type
class Mutation:
    @strawberry.mutation
    def addFavouriteCity(self, city: str, userName: str) -> str:
        return add_favourite_city_for_user(city,userName)
import strawberry
from typing import List

@strawberry.type
class WeatherData:
    date: str
    city: str
    times: List[str]
    temperatures: List[float]
    humidities: List[float]
import pytest 
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

def test_city_date_query():
    query = """
        query TestQuery {
            getWeatherData(city: $city, date: "2023-02-23")
            {
                temperatures
                humidities
                times
            }
            """

    result = schema.execute_sync(query,
                                 variable_values={"city": "London", "date": "2023-02-23"})

    assert result.errors is None
    assert result.data["times"] ==["2023-02-22 00:00", "2023-02-22 01:00", "2023-02-22 02:00", "2023-02-22 03:00", "2023-02-22 04:00", "2023-02-22 05:00", "2023-02-22 06:00", "2023-02-22 07:00", "2023-02-22 08:00", "2023-02-22 09:00", "2023-02-22 10:00", "2023-02-22 11:00", "2023-02-22 12:00", "2023-02-22 13:00", "2023-02-22 14:00", "2023-02-22 15:00", "2023-02-22 16:00", "2023-02-22 17:00", "2023-02-22 18:00", "2023-02-22 19:00", "2023-02-22 20:00", "2023-02-22 21:00", "2023-02-22 22:00", "2023-02-22 23:00"] 
    assert result.data["temperatures"] == [46.4, 46.1, 45.8, 45.5, 45.6, 45.7, 45.9, 46.3, 46.7, 47.1, 48.9, 50.7, 52.5, 51.4, 50.4, 49.3, 48.1, 46.9, 45.7, 44.9, 44.1, 43.3, 42.5, 41.7] 
    assert result.data["humidities"] ==[88.0, 84.0, 81.0, 77.0, 79.0, 81.0, 83.0, 85.0, 86.0, 88.0, 81.0, 74.0, 68.0, 71.0, 75.0, 78.0, 77.0, 76.0, 75.0, 74.0, 74.0, 73.0, 76.0, 79.0] 

from tests.conftest import TestAsynchronously
from tests.graphql.queries import london_23feb2023_query, invalid_city_query, pmcb_favourite_city
from tests.graphql.mutations import * #* not good practice but assume okay in this case
from src.app import schema

class TestUsers(TestAsynchronously):

    def test_01_verify_london_weather_for_date(self):
        result = schema.execute_sync(
            london_23feb2023_query,
        )
        assert result.data['getWeatherData']["times"] ==["2023-02-23 00:00", "2023-02-23 01:00", "2023-02-23 02:00", "2023-02-23 03:00", "2023-02-23 04:00", "2023-02-23 05:00", "2023-02-23 06:00", "2023-02-23 07:00", "2023-02-23 08:00", "2023-02-23 09:00", "2023-02-23 10:00", "2023-02-23 11:00", "2023-02-23 12:00", "2023-02-23 13:00", "2023-02-23 14:00", "2023-02-23 15:00", "2023-02-23 16:00", "2023-02-23 17:00", "2023-02-23 18:00", "2023-02-23 19:00", "2023-02-23 20:00", "2023-02-23 21:00", "2023-02-23 22:00", "2023-02-23 23:00"] 
        assert result.data['getWeatherData']["temperatures"] == [40.8, 40.5, 40.1, 39.7, 39.6, 39.4, 39.2, 39.8, 40.4, 41.0, 42.8, 44.6, 46.4, 46.2, 45.9, 45.7, 45.6, 45.4, 45.3, 43.7, 42.1, 40.5, 40.0, 39.5]
        assert result.data['getWeatherData']["humidities"] == [83.0, 82.0, 81.0, 81.0, 81.0, 81.0, 81.0, 84.0, 86.0, 89.0, 80.0, 71.0, 63.0, 63.0, 64.0, 65.0, 65.0, 66.0, 66.0, 68.0, 69.0, 71.0, 70.0, 70.0]


    def test_02_invalid_weather_api_response(self):
        result = schema.execute_sync(
            invalid_city_query,
        )
        assert result.data is None
        assert result.errors[0].message == "API returned no data. Check city and date values."


    def test_03_mutation_valid_user_valid_city(self):
        result = schema.execute_sync(
            valid_user_valid_city,
        )
        assert result.data['addFavouriteCity']== "Added Dublin to favourites for user cat"
        from src.graphql.db.dict_based import city_db
        assert city_db['cat'] == "Dublin"

    def test_04_mutation_valid_user_invalid_city(self):
        result = schema.execute_sync(
            valid_user_invalid_city,
        )
        #INTENTIONALLY ALLOWING USER TO IMPLEMENT ANY CITY THEY WANT -> MAY NOT BE ON WEATHER DB BUT WILL BE ADDED TO FAVOURITES
        assert result.data['addFavouriteCity']== "Added D to favourites for user cat"

    def test_05_invalid_user_valid_city(self):
        result = schema.execute_sync(
            invalid_user_valid_city,
        )
        assert result.data['addFavouriteCity']== "User iamnotauser does not exist"


    def test_06_invalid_user_invalid_city(self):
        result = schema.execute_sync(
            invalid_user_invalid_city,
        )
        assert result.data['addFavouriteCity']== "User iamnotauser does not exist"

    def test_07_pmcb_favourite_city_not_set(self):
        result = schema.execute_sync(
            pmcb_favourite_city,
        )
        assert result.data['getFavouriteCity']== "NULL"

    def test_08_pmcb_favourite_city(self):
        from src.graphql.db.dict_based import city_db
        city_db['pmcb'] = "Dublin"
        result = schema.execute_sync(
            pmcb_favourite_city,
        )
        assert result.data['getFavouriteCity']== "Dublin"
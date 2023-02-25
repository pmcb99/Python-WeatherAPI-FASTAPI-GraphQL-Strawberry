import datetime 

today = datetime.date.today()
todays_date = today.strftime("%Y-%m-%d")

london_23feb2023_query = """
    query TestQuery {
        getWeatherData(city: "London", date: "2023-02-23")
        {
            temperatures
            humidities
            times
        }
    }
        """

invalid_city_query = """query TestQuery {
        getWeatherData(city: "L", date: "2023-02-23")
        {
            temperatures
            humidities
            times
        }
}
"""

invalid_date_query = """query TestQuery {
        getWeatherData(city: "London", date: "2023-F2-23")
        {
            temperatures
            humidities
            times
        }
}
"""



pmcb_favourite_city = """query TestQuery3 {
  getFavouriteCity(userName: "pmcb")
}
"""

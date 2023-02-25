london_23feb2023_query = """
    query TestQuery {
        getWeatherData(city: "London", date: "2023-02-23")
        {
            temperatures
            humidities
            times
        }
        """

newyork_22feb2023_query = """
    query TestQuery2 {
        getWeatherData(city: "London", date: "2023-02-23")
        {
            temperatures
            humidities
            times
        }
        """

pmcb_favourite_city = """query TestQuery3 {
  getFavouriteCity(userName: "pmcb")
}
"""

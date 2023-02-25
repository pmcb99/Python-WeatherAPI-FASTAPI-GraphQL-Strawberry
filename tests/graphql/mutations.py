valid_user_valid_city= """mutation {
  addFavouriteCity(city: "Dublin", userName: "cat")
}
"""

valid_user_invalid_city= """mutation {
  addFavouriteCity(city: "D", userName: "cat")
}
"""

invalid_user_valid_city= """mutation {
  addFavouriteCity(city: "Dublin", userName: "iamnotauser")
}
"""

invalid_user_invalid_city= """mutation {
  addFavouriteCity(city: "D", userName: "iamnotauser")
}
"""

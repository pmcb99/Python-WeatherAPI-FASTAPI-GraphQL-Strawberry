from config.config import DevConfig
import uvicorn
from src.app import create_app

app= create_app()

if __name__ == "__main__":
    print("Starting server...")
    uvicorn.run("main:app", reload=True)


'''
NOTES FOR CAT:
1. Decided to provide temp and hum data as list of floats.
   Seems logical for an end user who wants to use data for a graph.
   Could have provided tuples of (time, temp, hum) or something like that
   Also tried having WeatherData temperature be a list of Temperature objects
   As shown in the old main code Temperature and Humidity classes
   Lists seemed more intuitive but depends on use case for user
'''
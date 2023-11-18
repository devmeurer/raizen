# services/weather_service.py

import requests
from settings import settings


open_weather_api_key = settings.OPEN_WEATHER_API_KEY

def get_weather_data(city, country):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={open_weather_api_key}"   
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return str(e) 

def save_weather_data(weather_data, db):
    collection = db.weather_forecasts
    collection.insert_one(weather_data)
    return weather_data 

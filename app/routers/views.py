from fastapi import FastAPI

from app.services.weather_api import get_weather_data
from app.services.weather_api import save_weather_data
from app.database.config import get_mongo_db
from app.database.models import WeatherModel

app = FastAPI()

@app.get("/weather", response_model=WeatherModel)
async def get_weather(city: str, country: str):
    weather_data = get_weather_data(city, country)
    db = get_mongo_db()
    saved_data = save_weather_data(weather_data, db)
    return WeatherModel(**saved_data)

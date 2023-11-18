from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
class Coord(BaseModel):
    lon: float
    lat: float

class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str

class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int

class Wind(BaseModel):
    speed: float
    deg: int

class Clouds(BaseModel):
    all: int

class Sys(BaseModel):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int

class WeatherModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    coord: Coord
    weather: List[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    name: str
    cod: int

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

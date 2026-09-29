from sqlalchemy import (Float, Boolean, DateTime, String, Text, Integer)

flights_dtype={
    "iata": String(3),
    "delay": Float,
    "timezone": String(50),
    "schedule": DateTime,
    "airport": Text,
    "arrival": Boolean
}

meteo_dtype={
    "iata": String(3),
    "time": DateTime,
    "temp_2m": Float,
    "humidity_2m": Float,
    "weather_code": Integer, 
    "precipitation": Float,
    "wind_speed_10m": Float,
    "wind_direction_10m": Float,
    "cloud_cover": Float,
    "wind_gusts_10m": Float,
    "apparent_temp": Float
}
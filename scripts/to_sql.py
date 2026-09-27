from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import (Float, Boolean, DateTime, String, Text, Integer)
from sqlalchemy import text

load_dotenv("../.env")

# hail: mưa đá

DB_USER= os.getenv("DB_USER")
DB_PW= os.getenv("DB_PW")
DB_IP= os.getenv("DB_IP")
DB_PORT= os.getenv("DB_PORT")
DB_NAME= os.getenv("DB_NAME")

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PW}@{DB_IP}:{DB_PORT}/{DB_NAME}")

sql_weather = text("""
    CREATE TABLE IF NOT EXISTS weather(
        code INT,
        description VARCHAR(70)
    )
""")
sql_insert= text("""
    INSERT INTO weather (code, description)
    VALUES (:code, :description)

""")

weather_code_rows= [
    {"code": 0, "description": "Clear sky"},
    {"code": 1, "description": "Mainly clear"},
    {"code": 2, "description": "Partly cloudy"},
    {"code": 3, "description": "Overcast"}, # covered by thick clouds
    {"code": 45, "description": "Fog"},
    {"code": 48, "description": "Depositing rime fog"},
    {"code": 51, "description": "Light drizzle"},
    {"code": 53, "description": "Moderate drizzle"},
    {"code": 55, "description": "Dense drizzle"},
    {"code": 56, "description": "Light freezing drizzle"},
    {"code": 57, "description": "Dense freezing drizzle"},
    {"code": 61, "description": "Slight rain"},
    {"code": 63, "description": "Moderate rain"},
    {"code": 65, "description": "Heavy rain"},
    {"code": 66, "description": "Light freezing rain"},
    {"code": 67, "description": "Heavy freezing rain"},
    {"code": 71, "description": "Slight snowfall"},
    {"code": 73, "description": "Moderate snowfall"},
    {"code": 75, "description": "Heavy snowfall"},
    {"code": 77, "description": "Snow grains"},
    {"code": 80, "description": "Slight rain showers"},
    {"code": 81, "description": "Moderate rain showers"},
    {"code": 82, "description": "Violent rain showers"},
    {"code": 85, "description": "Slight snow showers"},
    {"code": 86, "description": "Heavy snow showers"},
    {"code": 95, "description": "Thunderstorm"},
    {"code": 96, "description": "Thunderstorm with slight hail"},
    {"code": 97, "description": "Heavy thunderstorm"},
    {"code": 99, "description": "Thunderstorm with heavy hail"}, 
]

flights= pd.read_csv("data/csv/flights.csv")
meteo= pd.read_csv("data/csv/meteo.csv")

# validation

flights["iata"]= flights["iata"].astype(str)
flights["timezone"]= flights["timezone"].astype(str)
flights["scheduled"]= pd.to_datetime(flights["scheduled"])
flights["airport"]= flights["airport"].astype(str)

meteo["iata"]= meteo["iata"].astype(str)
meteo["time"] = pd.to_datetime(meteo["time"])
meteo["temp_2m"]= meteo["temp_2m"].round(2)
meteo["humidity_2m"]= meteo["humidity_2m"].round(2)
meteo["weather_code"]= meteo["weather_code"].astype(int)
meteo["precipitation"]= meteo["precipitation"].round(2)
meteo["wind_speed_10m"]= meteo["wind_speed_10m"].round(2)
meteo["wind_direction_10m"]= meteo["wind_direction_10m"].round(2)
meteo["cloud_cover"]= meteo["cloud_cover"].round(2)
meteo["wind_gusts_10m"]= meteo["wind_gusts_10m"].round(2)
meteo["apparent_temp"]= meteo["apparent_temp"].round(2)

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


def weather_code(engine, sql_table, sql_insert, rows):
    with engine.begin() as conn:
        conn.execute(sql_table)
        conn.execute(sql_insert, rows)
        
        
def to_sql(engine, weather_sql, sql_insert, weather_rows, flights, meteo, flights_dtype, meteo_dtype):
    flights.to_sql("flights", engine, "flight_meteo", if_exists= "fail", index=False, method= "multi", dtype= flights_dtype)
    meteo.to_sql("meteo", engine, "flight_meteo", if_exists= "fail", index=False, method= "multi", dtype= meteo_dtype)
    weather_code(engine, weather_sql, sql_insert, weather_rows)


if __name__ == "__main__":
    to_sql(engine, sql_weather, sql_insert, weather_code_rows, flights, meteo, flights_dtype, meteo_dtype)


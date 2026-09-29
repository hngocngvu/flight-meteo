import pandas as pd
from sqlalchemy import text

from src.database.seeds import weather_code_rows
from src.database.schema import flights_dtype, meteo_dtype
from src.database.database import engine
from src.database.queries import sql_weather, sql_insert_weather


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


def weather_code(engine, sql_table, sql_insert_weather, rows):
    with engine.begin() as conn:
        conn.execute(sql_table)
        conn.execute(sql_insert_weather, rows)
        
        
def to_sql(engine, weather_sql, sql_insert_weather, weather_rows, flights, meteo, flights_dtype, meteo_dtype):
    flights.to_sql("flights", engine, "flight_meteo", if_exists= "fail", index=False, method= "multi", dtype= flights_dtype)
    meteo.to_sql("meteo", engine, "flight_meteo", if_exists= "fail", index=False, method= "multi", dtype= meteo_dtype)
    weather_code(engine, weather_sql, sql_insert_weather, weather_rows)


if __name__ == "__main__":
    to_sql(engine, sql_weather, sql_insert_weather, weather_code_rows, flights, meteo, flights_dtype, meteo_dtype)


from fastapi import FastAPI
from src.database.database import engine 
from sqlalchemy import text
from datetime import datetime

app = FastAPI()

@app.get("/flights")
async def get_flights(airport: str|None=None, scheduled: datetime|None=None, 
                      start: datetime|None=None, end: datetime|None=None):
    params= {
        "airport": f"%{airport}%",
        "scheduled": scheduled,
        "start": start,
        "end": end
    }

    with engine.connect() as conn:
        if scheduled is not None:
            query= text("""
        SELECT flights.airport, flights.scheduled, flights.timezone, flights.delay, flights.arrival, meteo.*, weather.description
        FROM flights JOIN meteo ON flights.iata= meteo.iata
        JOIN weather ON weather.code= meteo.weather_code
        WHERE (flights.airport LIKE :airport AND flights.scheduled= :scheduled AND flights.scheduled= meteo.time)
    """)
            result= conn.execute(query, params)

        elif start is not None and end is not None:
            query= text("""
        SELECT flights.airport, flights.scheduled, flights.timezone, flights.delay, flights.arrival, meteo.*, weather.description
        FROM flights JOIN meteo ON flights.iata= meteo.iata
        JOIN weather ON weather.code= meteo.weather_code
        WHERE (flights.airport LIKE :airport 
        AND (flights.scheduled >= :start AND flights.scheduled <= :end) AND flights.scheduled= meteo.time)
    """)
            result= conn.execute(query, params)

        return result.mappings().all() #convert to RowMapping- quite similar to dict()


@app.get("/meteo")
async def get_meteo(airport: str|None=None, time: datetime|None=None):
    params={
        "airport": f"%{airport}%",
        "time": time
    }
    with engine.connect() as conn:
        if airport is not None and time is not None:
            query= text("""
                    SELECT DISTINCT flights.airport, meteo.*, weather.description 
                    FROM meteo JOIN flights ON meteo.iata= flights.iata 
                    JOIN weather ON weather.code= meteo.weather_code
                    WHERE meteo.time= :time AND flights.airport LIKE :airport
                    """)
            result= conn.execute(query, params)

        elif time is not None and airport is None:
            query= text("""
                    SELECT DISTINCT flights.airport, meteo.*, weather.description 
                    FROM meteo JOIN flights ON meteo.iata= flights.iata 
                    JOIN weather ON weather.code= meteo.weather_code
                    WHERE meteo.time= :time
                    """)
            result= conn.execute(query, params)

        elif airport is not None and time is None: 
            query= text("""
                    SELECT DISTINCT flights.airport, meteo.*, weather.description 
                    FROM meteo JOIN flights ON meteo.iata= flights.iata 
                    JOIN weather ON weather.code= meteo.weather_code
                    WHERE flights.airport LIKE :airport
                    """)
            result= conn.execute(query, params)
    
        return result.mappings().all()

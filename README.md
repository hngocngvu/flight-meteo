# FlightMeteo

An end-to-end project that builds a data pipeline for collecting, transforming, integrating, and storing flight and airport weather data, followed by an AI application layer for querying and interacting with the processed data using natural language.

Current progress: The project is currently in the Data Engineering phase, focusing on API data ingestion, data transformation, database design, and FastAPI-based data access. The AI Engineering layer, including LLM-powered data interaction and tool/function calling, is planned as the next phase.

# Set up

- Create an **.env** file having the same level with dir **flight-meteo** with the variables in **.env.example**

- Create a python/conda environment and run:

```
pip install -r requirements.txt
```

# Run data crawling, processing & migration scripts 

## Data crawling

- Flights (https://api.aviationstack.com/v1/flights)

```
python scripts/crawl_flight.py
```

- Geographical location (lat & lon) of airports (https://airportsapi.com/api/airports/)

```
python scripts/crawl_geo.py
```

- Meteo data (in hours) of airports (https://archive-api.open-meteo.com/v1/archive)

```
python scripts/crawl_meteo.py
```

# Run API docs

```
uvicorn src.api.main:app --reload --port 8000
```


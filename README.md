# FlightMeteo

An end-to-end project that builds a data pipeline for collecting, transforming, integrating, and storing flight and airport weather data, followed by an AI application layer for querying and interacting with the processed data using natural language.

Current progress: The project is currently in the Data Engineering phase, focusing on API data ingestion, data transformation, database design, and FastAPI-based data access. The AI Engineering layer, including LLM-powered data interaction and tool/function calling, is planned as the next phase.

# Run data crawling, processing & migration scripts 

## Data crawling

- Flights (https://api.aviationstack.com/v1/flights)

```
python scripts/crawl_flight.py
```

- Flights (https://api.aviationstack.com/v1/flights)

```
python scripts/crawl_flight.py
```
# Run API docs

```
uvicorn src.api.main:app --reload --port 8000
```


from fastapi import FastAPI
from src.database.database import engine 
from sqlalchemy import text

app = FastAPI()

@app.get("/flights/{iata}")

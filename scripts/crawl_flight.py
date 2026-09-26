import requests
import os
from dotenv import load_dotenv
import json

load_dotenv("../.env")

aviation_api= os.getenv("AVIATION_API_KEY")
aviation_url= "https://api.aviationstack.com/v1/flights"


def get_data(url, api):
    params= {
        "access_key": api
    }
    r= requests.get(url, params= params)
    return r.json()

def crawl_flight(url, api, file="data/json/flight_data.json"):
    data= get_data(url, api)
    with open(file,"w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    crawl_flight(aviation_url, aviation_api)
    

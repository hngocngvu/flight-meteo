from dotenv import load_dotenv
import os


load_dotenv("../.env")


DB_USER= os.getenv("DB_USER")
DB_PW= os.getenv("DB_PW")
DB_IP= os.getenv("DB_IP")
DB_PORT= os.getenv("DB_PORT")
DB_NAME= os.getenv("DB_NAME")
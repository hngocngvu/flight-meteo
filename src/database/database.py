from sqlalchemy import create_engine
from config import DB_USER, DB_PW, DB_IP, DB_PORT, DB_NAME

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PW}@{DB_IP}:{DB_PORT}/{DB_NAME}")

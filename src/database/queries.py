from sqlalchemy import text

sql_weather = text("""
    CREATE TABLE IF NOT EXISTS weather(
        code INT,
        description VARCHAR(70)
    )
""")
sql_insert_weather= text("""
    INSERT INTO weather (code, description)
    VALUES (:code, :description)

""")
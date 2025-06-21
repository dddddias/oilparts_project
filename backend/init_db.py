import psycopg2
import os
from dotenv import load_dotenv

# Загрузим переменные окружения
load_dotenv()

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# Подключение к серверу без указания конкретной БД
conn = psycopg2.connect(
    dbname="postgres",
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
conn.autocommit = True

with conn.cursor() as cur:
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
    exists = cur.fetchone()
    if not exists:
        cur.execute(f'CREATE DATABASE "{DB_NAME}"')
        print(f"✅ База данных '{DB_NAME}' успешно создана.")
    else:
        print(f"ℹ️ База данных '{DB_NAME}' уже существует.")

conn.close()

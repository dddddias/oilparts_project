import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Загрузим переменные окружения
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# Строка подключения с использованием pg8000
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создаём Engine
engine = create_engine(DATABASE_URL, echo=True)

# Сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
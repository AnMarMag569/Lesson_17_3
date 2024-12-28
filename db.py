from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# движок базы данных
engine = create_engine('sqlite:///taskmanager.db', echo=True)

# объект сессии
SessionLocal = sessionmaker(bind=engine)

# базовый класс для моделей
class Base(DeclarativeBase):
    pass
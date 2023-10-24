from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from core.config import DATABASE_URL

# Configuracion de sqlalchemy y conexion a la base de datos mysql

engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()


class Database:
    def __init__(self):
        self.session = SessionLocal()
    def __enter__(self):
        return self.session
    def __exit__(self, exc_type, exc_value, traceback):
        print("CONEXION CERRADA")
        self.session.close()

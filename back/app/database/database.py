from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from core.config import DATABASE_URL

# SQLAlchemy configuration and connection to the MySQL database

engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()


class Database:
    """
    Database class to manage sessions using context managers.
    
    This provides a convenient way to manage session lifecycle by using the 'with' statement.
    """

    def __init__(self):
        self.session = SessionLocal()

    def __enter__(self):
        """
        Returns the database session instance when entering the context.
        """
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes the database session when exiting the context.
        """
        print("CONNECTION CLOSED")
        self.session.close()

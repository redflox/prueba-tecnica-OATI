from models.tutorial_detail_model import TutorialDetail
from models.tutorial_model import Tutorial
from database.database import engine


def create_tables():
    """
    Creates the necessary tables for the application.
    
    The 'tutorial_details' table is created first followed by the 'tutorials' table.
    """
    # Create the 'tutorial_details' table first
    TutorialDetail.__table__.create(bind=engine, checkfirst=True)
    
    # Then, create the 'tutorials' table
    Tutorial.__table__.create(bind=engine, checkfirst=True)

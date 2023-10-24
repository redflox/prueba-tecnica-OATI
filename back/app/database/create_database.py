from models.tutorial_detail_model import  TutorialDetail
from models.tutorial_model import Tutorial
from database.database import engine


def create_tables():
    # Crear la tabla 'tutorial_details' primero
    TutorialDetail.__table__.create(bind=engine, checkfirst=True)
    # Luego, crear la tabla 'tutorials'
    Tutorial.__table__.create(bind=engine, checkfirst=True)

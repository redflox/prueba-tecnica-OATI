from models.tutorial_model import Tutorial
from models.tutorial_detail_model import TutorialDetail
from database.database import Database
from services.exception import ResourceNotFound
from sqlalchemy.orm import joinedload


# Servicio de tutoriales
class TutorialService:
    def __init__(self):
        self.database = Database()

    # Crea un tutorial con detalle
    def create_tutorial_with_details(self, tutorial_data: dict, details_data: dict):
        with self.database as db:
            try:
                tutorial = Tutorial(**tutorial_data)
                detail = TutorialDetail(**details_data)
                
                db.add(tutorial)
                db.flush()
                db.refresh(tutorial)
                
                db.add(detail)
                db.flush()
                db.refresh(detail)
                
                tutorial.detail_id = detail.id
                db.commit()

                db.refresh(tutorial)
                db.refresh(detail)
                
                return tutorial, detail
            except Exception as e:
                db.rollback()
                raise e

    # Crea un tutorial
    def create_tutorial(self, tutorial_data):
        with self.database as db:
            try:
                tutorial = Tutorial(**tutorial_data)
                db.add(tutorial)
                db.commit()
                db.refresh(tutorial)
                return tutorial
            except Exception as e:
                db.rollback()
                raise e

    # Obtiene un tutorial con su id
    def get_tutorial_by_id(self, tutorial_id: int):
        with self.database as db:
            try:
                tutorial = db.query(Tutorial).filter(Tutorial.id == tutorial_id).first()
                return tutorial
            except Exception as e:
                db.rollback()
                raise e
            finally:
                db.close()

    # Obtiene todos los tutoriales
    def get_alls_tutorials(self):
        with self.database as db:
            try:
                tutorials = db.query(Tutorial).all()
                return tutorials
            except Exception as e:
                db.rollback()
                raise e
            
    # Obtiene todos los tutoriales con sus detalles
    def get_alls_tutorials_with_details(self):
        with self.database as db:
            try:
                tutorials = db.query(Tutorial).options(joinedload(Tutorial.detail)).all()
                result = [{
                    "id": tutorial.id,
                    "title": tutorial.title,
                    "description": tutorial.description,
                    "state": tutorial.state,
                    "detail": {
                        "id": tutorial.detail.id,
                        "creation_date": tutorial.detail.creation_date,
                        "creator_user": tutorial.detail.creator_user
                    } if tutorial.detail else None  # Si no hay detalle, se deja el campo vacío
                } for tutorial in tutorials]
                return result
            except Exception as e:
                db.rollback()
                raise e

    # Actualiza un tutorial
    def update_tutorial(self, tutorial_id: int, tutorial_data: dict):
        with self.database as db:
            try:
                tutorial = db.query(Tutorial).filter(Tutorial.id == tutorial_id).first()
                if not tutorial:
                    raise ResourceNotFound(f"Tutorial not exist with id {tutorial_id}")
                for key, value in tutorial_data.items():
                    setattr(tutorial, key, value)

                db.commit()
                db.refresh(tutorial)
                return tutorial
            except Exception as e:
                db.rollback()
                raise e

    # Elimina un tutorial
    def delete_tutorial(self, tutorial_id):
        with self.database as db:
            try:
                tutorial = db.query(Tutorial).filter(Tutorial.id == tutorial_id).first()
                if not tutorial:
                    raise ResourceNotFound(f"Tutorial with id {tutorial_id} not found")
                db.delete(tutorial)
                db.commit()
                return tutorial
            except Exception as e:
                db.rollback()
                raise e
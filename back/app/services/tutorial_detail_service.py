from services.exception import ResourceNotFound
from database.database import Database
from models.tutorial_model import Tutorial
from models.tutorial_detail_model import TutorialDetail

# Tutorial Detail Service
class TutorialDetailService:
    def __init__(self):
        self.database = Database()

    # Create tutorial detail
    def create_tutorial_detail(self, tutorial_id: int, detail_data: dict):
        with self.database as db:
            try:
                tutorial = db.query(Tutorial).filter(Tutorial.id == tutorial_id).first()
                if not tutorial:
                    raise ResourceNotFound(f"Tutorial with ID {tutorial_id} not found")
                
                if tutorial.detail_id is not None:
                    raise ValueError(f"Detail already exists for tutorial with ID {tutorial_id}")

                tutorial_detail = TutorialDetail(**detail_data)
                db.add(tutorial_detail)
                db.commit()
                db.refresh(tutorial_detail)

                tutorial.detail_id = tutorial_detail.id
                db.commit()

                return {
                    "id": tutorial_detail.id,
                    "creation_date": tutorial_detail.creation_date,
                    "creator_user": tutorial_detail.creator_user
                }
            except Exception as e:
                db.rollback()
                raise e

    # Get tutorial details
    def get_detail_for_tutorial(self, tutorial_id: int):
        with self.database as db:
            try:
                tutorial = db.query(Tutorial).filter(Tutorial.id == tutorial_id).first()
                if not tutorial:
                    raise ResourceNotFound(f"Tutorial with ID {tutorial_id} not found")
                
                if tutorial.detail_id is None:
                    raise ValueError(f"No detail exists for tutorial with ID {tutorial_id}")

                tutorial_detail = db.query(TutorialDetail).filter(TutorialDetail.id == tutorial.detail_id).first()
                if not tutorial_detail:
                    raise ResourceNotFound(f"Detail not found for tutorial with ID {tutorial_id}")

                return tutorial_detail
            except Exception as e:
                db.rollback()
                raise e

    # Update tutorial details
    def update_detail_by_id(self, tutorial_detail_id: int, detail_data: dict):
        with self.database as db:
            try:
                tutorial_detail = db.query(TutorialDetail).filter(TutorialDetail.id == tutorial_detail_id).first()
                if not tutorial_detail:
                    raise ResourceNotFound(f"Detail not found for tutorial with ID {tutorial_detail_id}")
                
                for key, value in detail_data.items():
                    setattr(tutorial_detail, key, value)

                db.commit()
                db.refresh(tutorial_detail)
                return tutorial_detail
            except Exception as e:
                db.rollback()
                raise e

    # Delete tutorial details
    def delete_detail_by_id(self, tutorial_detail_id: int):
        with self.database as db:
            try:
                tutorial_detail = db.query(TutorialDetail).filter(TutorialDetail.id == tutorial_detail_id).first()
                if not tutorial_detail:
                    raise ResourceNotFound(f"Detail not found for tutorial with ID {tutorial_detail_id}")

                db.delete(tutorial_detail)
                db.commit()
                return tutorial_detail
            except Exception as e:
                db.rollback()
                raise e

    # Get all tutorial details
    def get_all_details(self):
        with self.database as db:
            try:
                return db.query(TutorialDetail).all()
            except Exception as e:
                db.rollback()
                raise e

from sqlalchemy import Column, Integer, Date, String
from sqlalchemy.orm import relationship

# Importing Base which is used as the base class to define declarative models with SQLAlchemy.
from database.database import Base


class TutorialDetail(Base):
    """
    Data model representing the details of a tutorial. 
    This model is in a one-to-one relationship with the Tutorial model.
    """

    __tablename__ = "tutorial_details"

    id = Column(Integer,  primary_key=True, index=True)
    creation_date = Column(Date, index=True)
    creator_user = Column(String(255), index=True)

    tutorial = relationship("Tutorial", back_populates="detail", uselist=False)

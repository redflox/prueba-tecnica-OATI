from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# Importing Base which is used as the base class to define declarative models with SQLAlchemy.
from database.database import Base


class Tutorial(Base):
    """
    Data model representing a tutorial. 
    This model is in a one-to-one relationship with the TutorialDetail model.
    If the tutorial is deleted, its associated detail is also deleted.
    """

    __tablename__ = "tutorials"

    id = Column(Integer,  primary_key=True, nullable=False, autoincrement=True, index=True)
    title = Column(String(150), index=True)
    description = Column(String(1000))
    state = Column(Boolean, default=True)  # True indicates the tutorial is visible
    
    detail_id = Column(Integer, ForeignKey("tutorial_details.id"), nullable=True)
    detail = relationship("TutorialDetail", back_populates="tutorial", uselist=False, cascade="all, delete")

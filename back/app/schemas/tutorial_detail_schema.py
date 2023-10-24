from pydantic import BaseModel
from typing import Optional
from datetime import date

# Base schema for a tutorial detail.
class TutorialDetailBase(BaseModel):
    """
    Base schema representing the essential attributes of a tutorial detail.
    """
    creation_date: date
    creator_user: str

# Schema used for API data validation when creating a new tutorial detail.
class TutorialDetailCreate(TutorialDetailBase):
    """
    Schema for validating incoming data for creating a tutorial detail.
    """
    pass

# Schema interfacing with SQLAlchemy to handle database data for tutorial details.
class TutorialDetail(TutorialDetailBase):
    """
    Schema that includes the ID attribute for handling data from the database regarding tutorial details.
    """
    id: int

    class Config:
        from_attributes = True

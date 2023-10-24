from pydantic import BaseModel

# Base schema for a tutorial.
class TutorialBase(BaseModel):
    """
    Base schema representing the essential attributes of a tutorial.
    """
    title: str
    description: str
    state: bool

# Schema used for API data validation when creating a new tutorial.
class TutorialCreate(TutorialBase):
    """
    Schema for validating incoming data for creating a tutorial.
    """
    pass

# Schema interfacing with SQLAlchemy to handle database data for tutorials.
class Tutorial(TutorialBase):
    """
    Schema that includes the ID attribute for handling data from the database regarding tutorials.
    """
    id: int

    class Config:
        from_attributes = True

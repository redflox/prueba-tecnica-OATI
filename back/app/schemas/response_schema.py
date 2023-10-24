from pydantic import BaseModel
from datetime import date

# Pydantic schemas used for data validation and deserialization.

class TutorialResponse(BaseModel):
    """
    Data schema representing a tutorial for a more generic response.
    """
    id: int
    title: str
    description: str
    state: bool

class TutorialDetailResponse(BaseModel):
    """
    Data schema representing tutorial details for a more generic response.
    """
    id: int
    creation_date: date
    creator_user: str

class ResponseTutorialWithDetails(BaseModel):
    """
    Data schema used to respond with full details of a tutorial including its associated details.
    """
    tutorial: TutorialResponse
    details: TutorialDetailResponse

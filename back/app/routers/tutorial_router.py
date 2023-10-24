# Native and third-party imports
from fastapi import APIRouter, HTTPException, Depends, Body
from typing import List

# Schemas and services
from schemas.tutorial_schema import TutorialCreate, Tutorial
from schemas.tutorial_detail_schema import TutorialDetailCreate
from schemas.response_schema import ResponseTutorialWithDetails
from services.tutorial_service import TutorialService

# Custom exceptions located in the services folder
from services.exception import ResourceNotFound

# APIRouter instance for endpoints generation
tutorialRouter = APIRouter()

# Service instance for tutorial business logic
tutorial_service = TutorialService()

@tutorialRouter.get("/detail", response_model=list)
def get_all_tutorials_with_details():
    """
    Retrieves all tutorials with their respective details.
    """
    try:
        tutorials_with_details = tutorial_service.get_all_tutorials_with_details()
        return tutorials_with_details
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@tutorialRouter.get("/{tutorial_id}", response_model=Tutorial)
def read_tutorial(tutorial_id: int):
    """
    Retrieves a specific tutorial by its ID without the details.
    """
    tutorial = tutorial_service.get_tutorial_by_id(tutorial_id)
    if not tutorial:
        raise HTTPException(status_code=404, detail="Tutorial not found")
    return tutorial

@tutorialRouter.get("/", response_model=List[Tutorial])
def list_tutorials():
    """
    Retrieves all tutorials without details.
    """
    return tutorial_service.get_all_tutorials()

@tutorialRouter.post("/", response_model=Tutorial, status_code=201)
def create_tutorial(tutorial: TutorialCreate):
    """
    Stores a tutorial without associating any details.
    """
    return tutorial_service.create_tutorial(tutorial.dict())

@tutorialRouter.post("/detail", response_model=ResponseTutorialWithDetails)
def create_tutorial_with_details(tutorial: TutorialCreate = Body(...), details: TutorialDetailCreate = Body(...)):
    """
    Stores a tutorial and its associated details.
    """
    try:
        tutorial_created, detail_created = tutorial_service.create_tutorial_with_details(tutorial.dict(), details.dict())
        return {"tutorial": tutorial_created, "details": detail_created}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@tutorialRouter.patch("/{tutorial_id}", response_model=Tutorial)
def update_tutorial(tutorial_id: int, tutorial_data: dict):
    """
    Updates a tutorial without considering the details.
    """
    updated_tutorial = tutorial_service.update_tutorial(tutorial_id, tutorial_data)
    if not updated_tutorial:
        raise HTTPException(status_code=404, detail="Tutorial not found")
    return updated_tutorial

@tutorialRouter.delete("/{tutorial_id}", response_model=Tutorial)
def delete_tutorial(tutorial_id: int):
    """
    Deletes a tutorial and its associated details.
    """
    try:
        tutorial = tutorial_service.delete_tutorial(tutorial_id)
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail="Tutorial not found")
    return tutorial

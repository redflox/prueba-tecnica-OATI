# Native and third-party imports
from fastapi import APIRouter, HTTPException
from typing import List

# Schemas and services
from schemas.tutorial_detail_schema import TutorialDetail, TutorialDetailCreate
from services.tutorial_detail_service import TutorialDetailService
from services.exception import ResourceNotFound

# APIRouter instance for endpoint generation
tutorial_detail_router = APIRouter()

# Service instance for tutorial detail business logic
tutorial_detail_service = TutorialDetailService()

@tutorial_detail_router.get("/all", response_model=List[TutorialDetail])
def read_all_details():
    """
    Retrieves all existing details.
    """
    try:
        details = tutorial_detail_service.get_all_details()
        return details
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading details: {str(e)}")

@tutorial_detail_router.get("/{tutorial_id}/detail", response_model=TutorialDetail)
def read_detail_for_tutorial(tutorial_id: int):
    """
    Retrieves a detail by its ID.
    """
    try:
        detail = tutorial_detail_service.get_detail_for_tutorial(tutorial_id)
        return detail
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading detail for tutorial: {str(e)}")

@tutorial_detail_router.post("/{tutorial_id}/detail", response_model=TutorialDetail, status_code=201)
def create_detail_for_tutorial(tutorial_id: int, details: TutorialDetailCreate):
    """
    Stores a detail and associates it to a tutorial if possible.
    """
    try:
        detail_created = tutorial_detail_service.create_tutorial_detail(tutorial_id, details.dict())
        return detail_created
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating detail for tutorial: {str(e)}")

@tutorial_detail_router.patch("/{tutorial_detail_id}", response_model=TutorialDetail)
def update_detail_by_id(tutorial_detail_id: int, tutorial_detail_data: dict):
    """
    Updates the detail by its ID.
    """
    try:
        detail = tutorial_detail_service.update_detail_by_id(tutorial_detail_id, tutorial_detail_data)
        return detail
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating detail: {str(e)}")

@tutorial_detail_router.delete("/{tutorial_detail_id}", response_model=TutorialDetail)
def delete_detail_by_id(tutorial_detail_id: int):
    """
    Deletes the detail by its ID. The tutorial is not deleted.
    """
    try:
        detail = tutorial_detail_service.delete_detail_by_id(tutorial_detail_id)
        return detail
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting detail: {str(e)}")

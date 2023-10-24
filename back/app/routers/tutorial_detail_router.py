# Importaciones nativas y de librerias
from fastapi import APIRouter, HTTPException
from typing import List

# Esquemas y servicios
from schemas.tutorial_detail_schema import TutorialDetail, TutorialDetailCreate
from services.tutorial_detail_service import TutorialDetailService
from services.exception import ResourceNotFound

# Instancia de objeto de APIRouter para generar los endpoints
tutorial_detail_router = APIRouter()

# Instancia del servicio que controla la logica de negocio de detalles de tutoriales
tutorial_detail_service = TutorialDetailService()


# Este endpoint retorna todos los detalles existentes
@tutorial_detail_router.get("/all", response_model=List[TutorialDetail])
def read_all_details():
    try:
        details = tutorial_detail_service.get_all_details()
        return details
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=(f"Error reading details {str(e)}"))
    
# Este endpoint retorna un detalle a partir del id
@tutorial_detail_router.get("/{tutorial_id}/detail", response_model=TutorialDetail)
def read_detail_for_tutorial(tutorial_id: int):
    try:
        detail = tutorial_detail_service.get_detail_for_tutorial(tutorial_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=(f"Error reading detail for tutorial {str(e)}"))
    return detail

# Este endpoint guarda un detalle y lo asocia a un tutorial si es posible
@tutorial_detail_router.post("/{tutorial_id}/detail", response_model=TutorialDetail, status_code=201)
def create_detail_for_tutorial(tutorial_id: int, details: TutorialDetailCreate):
    try:
        detail_created = tutorial_detail_service.create_tutorial_detail(tutorial_id, details.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=(f"Error creating detail for tutorial {str(e)}"))
    return detail_created

# Este endpoint edita  el detalle a partir de su id
@tutorial_detail_router.patch("/{tutorial_detail_id}", response_model=TutorialDetail)
def update_detail_by_id(tutorial_detail_id: int, tutorial_detail_data: dict):
    try:
        detail = tutorial_detail_service.update_detail_by_id(tutorial_detail_id, tutorial_detail_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=(f"Error updating detail {str(e)}"))
    return detail

# Este endpoint elimina el detalle, no se elimina el tutorial.
@tutorial_detail_router.delete("/{tutorial_detail_id}", response_model=TutorialDetail)
def delete_detail_by_id(tutorial_detail_id: int):
    try:
        detail = tutorial_detail_service.delelte_detail_by_id(tutorial_detail_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=(f"Error deleting detail {str(e)}"))
    return detail

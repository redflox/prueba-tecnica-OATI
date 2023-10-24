# Importaciones nativas y de librerias
from fastapi import APIRouter,HTTPException, Depends, Body
from typing import List

# Esquemas y servicios
from schemas.tutorial_schema import TutorialCreate, Tutorial
from schemas.tutorial_detail_schema import TutorialDetailCreate
from schemas.response_schema import ResponseTutorialWithDetails
from services.tutorial_service import TutorialService

# Exepciones personalizadas en la carpeta service
from services.exception import ResourceNotFound

# Instancia de objeto de APIRouter para generar los endpoints
tutorialRouter = APIRouter()

# Instancia del servicio que controla la logica de negocio de tutoriales
tutorial_service = TutorialService()


# Este endpoint retorna todos los tutoriales con sus detalles.
@tutorialRouter.get("/datail", response_model=list)
def get_all_tutorials_with_details():
    try:
        tutorials_with_details = tutorial_service.get_alls_tutorials_with_details()
        return tutorials_with_details
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Este endpoint retorna un tutorial a partir del id pero sin detalles
@tutorialRouter.get("/{tutorial_id}", response_model=Tutorial)
def read_tutorial(tutorial_id: int):
    tutorial = tutorial_service.get_tutorial_by_id(tutorial_id)
    if not tutorial:
        raise HTTPException(status_code=404, detail="Could not find tutorial")
    return tutorial

# Este endpoint retorna todos los tutoriales sin detalles
@tutorialRouter.get("/", response_model=List[Tutorial])
def list_tutorials():
    return tutorial_service.get_alls_tutorials()

# Este endpoint guarda un tutorial sin detalle
@tutorialRouter.post("/", response_model=Tutorial,status_code=201)
def create_tutorial(tutorial: TutorialCreate):
    return tutorial_service.create_tutorial(tutorial.dict())

# Este endpoint guarda un tutorial con detalle
@tutorialRouter.post("/datail", response_model=ResponseTutorialWithDetails)
def create_tutorial_with_details(tutorial: TutorialCreate = Body(...), details: TutorialDetailCreate = Body(...)):
    try:
        tutorial_created, detail_created = tutorial_service.create_tutorial_with_details(tutorial.dict(), details.dict())
        return {"tutorial": tutorial_created, "details": detail_created}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Este endpoint edita un tutorial sin tener en cuenta los detalles.
@tutorialRouter.patch("/{tutorial_id}", response_model=Tutorial)
def update_tutorial(tutorial_id: int, tutorial_data: dict):
    update_tutorial = tutorial_service.update_tutorial(tutorial_id, tutorial_data)
    if not update_tutorial:
        raise HTTPException(status_code=404, detail="Could not find tutorial")
    return update_tutorial

# Este endpoint elimina un tutorial y su detalle asociado
@tutorialRouter.delete("/{tutorial_id}", response_model=Tutorial)
def delete_tutorial(tutorial_id: int):
    try:
        tutorial = tutorial_service.delete_tutorial(tutorial_id)
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail="Could not find tutorial")
    return tutorial
from pydantic import BaseModel
from datetime import date

# Esquemas de pydantic, funcionan para  validar datos y deserializar datos.


# Esquema de tutoriales para construir esquema mas generico.
class TutorialResponse(BaseModel):
    id: int
    title: str
    description: str
    state: bool

# Esquema de detalles para construir esquema mas generico.
class TutorialDetailResponse(BaseModel):
    id: int
    creation_date: date
    creator_user: str

# Esquema para responder todos los tutoriales con detalles
class ResponseTutorialWithDetails(BaseModel):
    tutorial: TutorialResponse
    details: TutorialDetailResponse
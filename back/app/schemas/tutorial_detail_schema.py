from pydantic import BaseModel
from typing import Optional
from datetime import date


# Esquema base de un detalle
class TutorialDetailBase(BaseModel):
    creation_date: date
    creator_user: str

# Este esquema que se usa para validar los datos de llegada al api respecto al detalle
class TutorialDetailCreate(TutorialDetailBase):
    pass

# Esquema que se usa con alchemy para manejar los datos de la db
class TutorialDetail(TutorialDetailBase):
    id: int

    class Config:
        from_attributes = True


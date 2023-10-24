from pydantic import BaseModel


# Esquema base para  un tutorial
class TutorialBase(BaseModel):
    title: str
    description: str
    state: bool


# Esquema para validar datos de  llegada al api respecto a un tutorial
class TutorialCreate(TutorialBase):
    pass

# Esquema para trabajar de la mano con sqlalchemy y datos provenientes de la db
class Tutorial(TutorialBase):
    id: int

    class Config:
        from_attributes = True
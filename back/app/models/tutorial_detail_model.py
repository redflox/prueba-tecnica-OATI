from sqlalchemy import Column, Integer, Date, String
from sqlalchemy.orm import relationship, backref

# Importando Base que se usa como clase base para definir modelos declarativos con sqlalchemy
from database.database import Base


# Modelo de datos para el detalle, esta relacionado 1 a 1 con el tutorial.
class TutorialDetail(Base):
    __tablename__ = "tutorial_details"

    id = Column(Integer,  primary_key=True, index=True)
    creation_date = Column(Date, index=True)
    creator_user = Column(String(255), index=True)

    tutorial = relationship("Tutorial", back_populates="detail", single_parent=True)

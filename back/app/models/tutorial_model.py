from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# Importando Base que se usa como clase base para definir modelos declarativos con sqlalchemy
from database.database import Base


# Modelo de datos para el tutorial, esta asociado 1 a 1 con el detalle, si se elimina el tutorial se elimina el detalle asociado.
class Tutorial(Base):
    __tablename__ = "tutorials"

    id = Column(Integer,  primary_key=True, nullable=False, autoincrement=True, index=True)
    title = Column(String(150), index=True)
    description = Column(String(1000))
    state = Column(Boolean, default=True)
    
    detail_id = Column(Integer, ForeignKey("tutorial_details.id"), nullable=True)
    detail = relationship("TutorialDetail", back_populates="tutorial", uselist=False, cascade="all, delete")

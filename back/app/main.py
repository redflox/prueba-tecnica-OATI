# Importaciones de fast api
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importacion para crear  tablas de la db
from database.create_database import create_tables

# Importando routers que componen el API REST
from routers.tutorial_router import tutorialRouter
from routers.tutorial_detail_router import tutorial_detail_router

# Funcion que crea las tablas en la base de datos
create_tables()

# Intancia de fastapi
app = FastAPI()

# Configurando cors
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agregando routers al api
app.include_router(tutorialRouter, prefix="/api/tutorial")
app.include_router(tutorial_detail_router, prefix="/api/tutorialdetail")
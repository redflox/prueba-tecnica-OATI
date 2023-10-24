import os
from dotenv import load_dotenv

load_dotenv(".env")

# Configuracion global del proyecto a partir de un archivo .env a  la altura del fichero main.py

DATABASE_URL = os.getenv("DATABASE_URL")
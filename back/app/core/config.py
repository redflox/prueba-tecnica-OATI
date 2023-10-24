import os
from dotenv import load_dotenv

load_dotenv(".env")

# Global project configuration sourced from an .env file at the root level (alongside main.py)

DATABASE_URL = os.getenv("DATABASE_URL")

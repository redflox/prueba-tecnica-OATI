# FastAPI imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import for database table creation
from database.create_database import create_tables

# Import routers for the REST API
from routers.tutorial_router import tutorialRouter
from routers.tutorial_detail_router import tutorial_detail_router

# Create the database tables (if they don't exist)
create_tables()

# Initialize FastAPI instance
app = FastAPI()

# Configure CORS
# WARNING: Allowing all origins for CORS can be insecure. 
# Limit to known origins in a production environment.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routers to the API
app.include_router(tutorialRouter, prefix="/api/tutorial")
app.include_router(tutorial_detail_router, prefix="/api/tutorialdetail")

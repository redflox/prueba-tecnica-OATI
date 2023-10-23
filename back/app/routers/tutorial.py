from fastapi import APIRouter

tutorialRouter = APIRouter()

@tutorialRouter.get("/")
async def hello_world():
    return {"message": "Hello World"}
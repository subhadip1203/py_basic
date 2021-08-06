
from fastapi import FastAPI

from app.api.v1 import api_router
from app.core import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Ping Success"}


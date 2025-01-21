"""Module for health routes."""
from fastapi import APIRouter, status

health_router = APIRouter()

@health_router.get("/liveness_probe", status_code=status.HTTP_200_OK)
async def health_check():
    """Checks if the api started correctly."""
    return {"status": "API is live"}

@health_router.get("/readiness_probe", status_code=status.HTTP_200_OK)
async def readiness_check():
    """Checks if the api is ready."""
    return {"status": "API is ready"}
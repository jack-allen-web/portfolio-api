from fastapi.middleware.cors import CORSMiddleware
from app.config import ALLOWED_ORIGINS
from fastapi import FastAPI

def add_cors_middleware(app: FastAPI):
    """
    Function to add CORS middleware to the FastAPI app.
    It uses the allowed origins from config.py.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,  # CORS allowed origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allows all headers
    )

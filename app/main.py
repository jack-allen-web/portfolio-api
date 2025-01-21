from fastapi import FastAPI

from app.middleware.cors import add_cors_middleware
from app.routes.health_routes import health_router
from app.routes.contact_routes import contact_router
from app.routes.project_routes import project_router

app = FastAPI()

add_cors_middleware(app)

app.include_router(health_router)
app.include_router(contact_router)
app.include_router(project_router)

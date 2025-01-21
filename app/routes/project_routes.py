"""Module containing project routes."""
from typing import List
from fastapi import APIRouter, status
from app.models.project import Project, TechStack

project_router = APIRouter()

projects = [
    Project(
        name="Portfolio Website",
        description="A personal portfolio built with FastAPI and React.",
        tech_stack=[TechStack.FAST_API, TechStack.REACT, TechStack.SQL],
        repo_link="https://github.com/jack-allen-web/portfolio-api",
        demo_link="https://yourportfoliosite.com"
    ),
    Project(
        name="E-commerce API",
        description="Backend for an e-commerce application with order management.",
        tech_stack=[TechStack.FAST_API, TechStack.MONDO_DB, TechStack.STRIPE],
        repo_link="https://github.com/yourusername/ecommerce-api",
        demo_link="https://yourapi.com"
    )
]

@project_router.get("/projects", response_model=List[Project], status_code=status.HTTP_200_OK)
async def get_projects():
    """Retrieve all projects."""
    return projects

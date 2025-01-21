"""Module containing project routes."""
from typing import List
from fastapi import APIRouter, status
from app.models.project import Project

project_router = APIRouter()

projects = [
    Project(
        name="Portfolio Website",
        description="A personal portfolio built with FastAPI and React.",
        tech_stack=["FastAPI", "React", "CSS", "PostgreSQL"],
        repo_link="https://github.com/yourusername/portfolio",
        demo_link="https://yourportfoliosite.com"
    ),
    Project(
        name="E-commerce API",
        description="Backend for an e-commerce application with order management.",
        tech_stack=["FastAPI", "MongoDB", "Stripe"],
        repo_link="https://github.com/yourusername/ecommerce-api",
        demo_link="https://yourapi.com"
    )
]


@project_router.get("/projects", response_model=List[app.models.project.Project], status_code=status.HTTP_200_OK)
async def get_projects():
    """Retrieve all projects."""
    return projects

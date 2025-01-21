from typing import List
from pydantic import BaseModel, Field


class Project(BaseModel):
    name: str = Field(..., description="Project name")
    description: str = Field(..., description="Project description")
    tech_stack: List[str] = Field(..., description="Tech stack list")
    repo_link: str = Field(..., description="Project repo link")
    demo_link: str = Field(..., description="Project demo link")

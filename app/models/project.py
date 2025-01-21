"""Module containing Project model details"""
from enum import Enum
from typing import List
from pydantic import BaseModel, Field

class TechStack(Enum):
    """
    Enum for TechStack model
    """
    PYTHON = "python"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    FAST_API = "fast-api"
    STRIPE = "stripe"
    REACT = "react"
    SQL = "sql"
    MONDO_DB = "mongodb"

class Project(BaseModel):
    """
    Project model
    """
    name: str = Field(..., description="Project name")
    description: str = Field(..., description="Project description")
    tech_stack: List[TechStack] = Field(..., description="Tech stack list")
    repo_link: str = Field(..., description="Project repo link")
    demo_link: str = Field(..., description="Project demo link")

from pydantic import BaseModel, Field


class ContactForm(BaseModel):
    name: str = Field(..., title="Name")
    email: str = Field(..., title="Email")
    message: str = Field(..., title="Message", min_length=10, max_length=5000)
    
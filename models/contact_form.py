from pydantic import BaseModel, Field, EmailStr


class ContactForm(BaseModel):
    name: str = Field(..., title="Name")
    email: EmailStr = Field(..., title="Email")
    
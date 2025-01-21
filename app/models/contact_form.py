from pydantic import BaseModel, Field, EmailStr


class ContactForm(BaseModel):
    name: str = Field(..., title="Name")
    email: EmailStr = Field(..., title="Email")
    message: str = Field(..., title="Message", min_length=10, max_length=5000)
    
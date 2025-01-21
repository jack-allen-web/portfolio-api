from fastapi import APIRouter, HTTPException, status
from app.models.contact_form import ContactForm

contact_router = APIRouter()

@contact_router.post("/contact", status_code=status.HTTP_201_CREATED)
async def submit_contact_form(contact: ContactForm):
    """Handle contact form submissions."""
    # Log or process the contact form
    # todo: add some persistent logging here
    print(f"New contact form submission: {contact}")

    # (Optional) Simulate sending an email
    if not contact.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    return {"message": "Thanks for reaching out!"}
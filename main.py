from fastapi import FastAPI
from fastapi.openapi.models import Contact

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API providing endpoint to Jack Allen's Portfolio website."}


@app.get("/projects}")
async def projects():
    return {"message": "Not implemented."}


@app.post("/contact")
async def submit_contact_form(contact_form: ContactForm):
    return {"message": "Not implemented."}
# **Portfolio Backend**

This is the backend service for my personal portfolio website, built using FastAPI. It serves project data, handles contact form submissions, and acts as the foundation for showcasing my development skills. 

The backend is designed to be lightweight, scalable, and easily extensible.

---

## **Table of Contents**

1. [Features](#features)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Usage](#usage)
   - [Running the Development Server](#running-the-development-server)
   - [API Documentation](#api-documentation)
4. [Project Structure](#project-structure)
5. [Endpoints](#endpoints)
---

## **Features**

- Provides project data via a REST API.
- Accepts contact form submissions securely.
- Built with FastAPI for high performance and easy API development.
- Fully documented with OpenAPI (Swagger UI).
- Ready for deployment on modern platforms like Vercel or AWS.

---

## **Getting Started**

### **Prerequisites**
Make sure you have the following installed:
- Python 3.10 or higher
- `pip` (Python package manager)
- A virtual environment tool like `venv` or `conda`

### **Instalation**
1. Clone the repository:
   ```bash
   git clone https://github.com/jack-allen-web/portfolio-api.git
   cd portfolio-api
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Create a .env file for environment variables:
   ```bash
   EMAIL_USERNAME=your_email
   EMAIL_PASSWORD=your_password
   
   portfolio-api/
   ├── app/
   │   ├── main.py          # Application entry point
   │   ├── models/          # Pydantic models for data validation
   │   └── routes/          # API routes and endpoints
   ├── .env                 # Environment variables
   ├── requirements.txt     # Python dependencies
   ├── README.md            # Project documentation
   └── tests/               # Test suite for the API
   
   
---

## **Usage**

### **Running the development server**
Start the server using Uvicorn:

Visit the API at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### **API Documentation**

Interactive API documentation is automatically generated and available at /docs. It includes details about all available endpoints, request models, and responses

---

## **Project Structure**
   ```bash
   portfolio-api/
   ├── app/
   │   ├── main.py          # Application entry point
   │   ├── models/          # Pydantic models for data validation
   │   └── routes/          # API routes and endpoints
   ├── .env                 # Environment variables
   ├── requirements.txt     # Python dependencies
   ├── README.md            # Project documentation
   └── tests/               # Test suite for the API
   ```

---
## **Endpoints**

| Method | Endpoint         | Description                                   |
|--------|------------------|-----------------------------------------------|
| GET    | `/projects`      | Retrieves all projects.                      |
| POST   | `/contact`       | Submits a contact form.                      |
import os


ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', "http://localhost:3000").split(",")

from fastapi import FastAPI

from app.database import engine, Base
from app.api import blood_api

# Import models so SQLAlchemy can detect tables
from app.models import blood


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Lifeline Blood Network",
    description="Blood Emergency and Donor Management System",
    version="1.0.0"
)


# Register Blood Emergency APIs
app.include_router(
    blood_api.router
)


@app.get("/")
def home():
    return {
        "message": "Lifeline Blood Network API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "OK"
    }
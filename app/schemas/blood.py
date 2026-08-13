from pydantic import BaseModel
from datetime import datetime


# ---------- Blood Request ----------

class BloodRequestCreate(BaseModel):
    patient_name: str
    blood_group: str
    hospital_name: str
    location: str
    contact_number: str
    required_units: int
    urgency: str = "Normal"


class BloodRequestResponse(BloodRequestCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


# ---------- Blood Donor ----------

class BloodDonorCreate(BaseModel):
    name: str
    age: int
    blood_group: str
    phone: str
    city: str


class BloodDonorResponse(BloodDonorCreate):
    id: int
    available: bool
    created_at: datetime

    class Config:
        from_attributes = True
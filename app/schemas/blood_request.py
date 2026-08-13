from pydantic import BaseModel


class BloodRequestCreate(BaseModel):
    patient_name: str
    blood_group: str
    hospital_name: str
    location: str
    contact_number: str
    required_units: int
    urgency: str


class BloodRequestResponse(BloodRequestCreate):
    id: int
    status: str

    class Config:
        from_attributes = True


class DonorCreate(BaseModel):
    name: str
    age: int
    blood_group: str
    phone: str
    city: str


class DonorResponse(DonorCreate):
    id: int
    available: bool

    class Config:
        from_attributes = True
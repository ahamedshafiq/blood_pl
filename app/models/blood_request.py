from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from app.database import Base


class BloodDonor(Base):
    __tablename__ = "blood_donors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    blood_group = Column(String)
    phone = Column(String)
    city = Column(String)
    available = Column(Boolean, default=True)


class BloodRequest(Base):
    __tablename__ = "blood_requests"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    blood_group = Column(String)
    hospital_name = Column(String)
    location = Column(String)
    contact_number = Column(String)
    required_units = Column(Integer)
    urgency = Column(String)
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
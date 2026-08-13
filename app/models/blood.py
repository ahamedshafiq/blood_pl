from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from app.database import Base


class BloodDonor(Base):
    __tablename__ = "blood_donors"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    blood_group = Column(String, nullable=False)

    phone = Column(String, nullable=False)

    city = Column(String, nullable=False)

    available = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class BloodRequest(Base):
    __tablename__ = "blood_requests"

    id = Column(Integer, primary_key=True, index=True)

    patient_name = Column(
        String,
        nullable=False
    )

    blood_group = Column(
        String,
        nullable=False
    )

    hospital_name = Column(
        String,
        nullable=False
    )

    location = Column(
        String,
        nullable=False
    )

    contact_number = Column(
        String,
        nullable=False
    )

    required_units = Column(
        Integer,
        nullable=False
    )

    urgency = Column(
        String,
        default="Normal"
    )

    status = Column(
        String,
        default="Pending"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
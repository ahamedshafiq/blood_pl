from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.blood import (
    BloodRequestCreate,
    BloodDonorCreate
)

from app.services import (
    request_service,
    donor_service
)


router = APIRouter(
    prefix="/blood",
    tags=["Blood Emergency"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# -------- Blood Request APIs --------

@router.post("/request")
def create_request(
    data: BloodRequestCreate,
    db: Session = Depends(get_db)
):

    return request_service.create_blood_request(
        db,
        data
    )



@router.get("/requests")
def get_requests(
    db: Session = Depends(get_db)
):

    return request_service.get_all_blood_requests(
        db
    )



@router.put("/request/{request_id}/status")
def update_status(
    request_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    return request_service.update_request_status(
        db,
        request_id,
        status
    )



# -------- Donor APIs --------

@router.post("/donor")
def register_donor(
    data: BloodDonorCreate,
    db: Session = Depends(get_db)
):

    return donor_service.register_donor(
        db,
        data
    )



@router.get("/donors/{blood_group}")
def search_donors(
    blood_group: str,
    db: Session = Depends(get_db)
):

    return donor_service.get_donors_by_blood_group(
        db,
        blood_group
    )
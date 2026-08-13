from sqlalchemy.orm import Session

from app.models.blood import BloodRequest
from app.schemas.blood import BloodRequestCreate


def create_blood_request(
    db: Session,
    request_data: BloodRequestCreate
):

    new_request = BloodRequest(
        **request_data.model_dump()
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    return new_request



def get_all_blood_requests(
    db: Session
):

    return (
        db.query(BloodRequest)
        .order_by(BloodRequest.created_at.desc())
        .all()
    )



def update_request_status(
    db: Session,
    request_id: int,
    status: str
):

    request = (
        db.query(BloodRequest)
        .filter(
            BloodRequest.id == request_id
        )
        .first()
    )

    if request:
        request.status = status
        db.commit()
        db.refresh(request)

    return request
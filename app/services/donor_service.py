
from sqlalchemy.orm import Session

from app.models.blood import BloodDonor
from app.schemas.blood import BloodDonorCreate


def register_donor(
    db: Session,
    donor_data: BloodDonorCreate
):

    new_donor = BloodDonor(
        **donor_data.model_dump()
    )

    db.add(new_donor)
    db.commit()
    db.refresh(new_donor)

    return new_donor



def get_donors_by_blood_group(
    db: Session,
    blood_group: str
):

    return (
        db.query(BloodDonor)
        .filter(
            BloodDonor.blood_group == blood_group,
            BloodDonor.available == True
        )
        .all()
    )



def update_donor_availability(
    db: Session,
    donor_id: int,
    available: bool
):

    donor = (
        db.query(BloodDonor)
        .filter(
            BloodDonor.id == donor_id
        )
        .first()
    )

    if donor:
        donor.available = available
        db.commit()
        db.refresh(donor)

    return donor
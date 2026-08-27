from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.event import Event
from backend.models.event_attendee import EventAttendee

router = APIRouter(
    prefix="/profile",
    tags=["Events"]
)


@router.get("/{user_id}/events")
def user_events(
    user_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Event)
        .join(
            EventAttendee,
            Event.id ==
            EventAttendee.event_id
        )
        .filter(
            EventAttendee.user_id ==
            user_id
        )
        .all()
    )
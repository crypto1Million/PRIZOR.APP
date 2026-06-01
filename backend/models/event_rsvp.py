from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class EventRSVP(Base):

    __tablename__ = "event_rsvps"

    id = Column(Integer, primary_key=True)

    event_id = Column(
        Integer,
        ForeignKey("events.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    status = Column(
        String,
        default="going"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    event = relationship("Event")
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class EventCheckin(Base):

    __tablename__ = "event_checkins"

    id = Column(Integer, primary_key=True)

    event_id = Column(
        Integer,
        ForeignKey("events.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    checked_in_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    event = relationship("Event")
from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class EventAnalytics(Base):

    __tablename__ = "event_analytics"

    id = Column(Integer, primary_key=True)

    event_id = Column(
        Integer,
        ForeignKey("events.id")
    )

    impressions = Column(
        Integer,
        default=0
    )

    views = Column(
        Integer,
        default=0
    )

    attendees = Column(
        Integer,
        default=0
    )

    ticket_revenue = Column(
        Float,
        default=0
    )

    sponsor_revenue = Column(
        Float,
        default=0
    )

    recorded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    event = relationship("Event")
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    JSON
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CreatorAnalyticsEvent(Base):

    __tablename__ = "creator_analytics_events"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    event_type = Column(
        String,
        nullable=False
    )

    event_source = Column(
        String
    )

    event_metadata = Column(JSON)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship(
        "User",
        back_populates="creator_analytics_events"
    )
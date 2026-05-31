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


class CallAnalytics(Base):

    __tablename__ = "call_analytics"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    call_id = Column(
        Integer,
        ForeignKey("video_calls.id"),
        nullable=False
    )

    duration_seconds = Column(
        Integer,
        default=0
    )

    average_latency_ms = Column(
        Float,
        default=0
    )

    packet_loss_percent = Column(
        Float,
        default=0
    )

    reconnect_count = Column(
        Integer,
        default=0
    )

    recorded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    call = relationship("VideoCall")
from sqlalchemy import (
    Column, Integer, Float,
    DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class StreamAnalytics(Base):

    __tablename__ = "stream_analytics"

    id = Column(Integer, primary_key=True, index=True)

    stream_id = Column(
        Integer,
        ForeignKey("live_streams.id")
    )

    peak_viewers = Column(
        Integer,
        default=0
    )

    unique_viewers = Column(
        Integer,
        default=0
    )

    total_watch_time = Column(
        Float,
        default=0
    )

    total_messages = Column(
        Integer,
        default=0
    )

    total_gifts = Column(
        Float,
        default=0
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    stream = relationship("LiveStream")
from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class StreamRecording(Base):

    __tablename__ = "stream_recordings"

    id = Column(Integer, primary_key=True, index=True)

    stream_id = Column(
        Integer,
        ForeignKey("live_streams.id")
    )

    storage_url = Column(String)

    duration_seconds = Column(
        Integer,
        default=0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    stream = relationship("LiveStream")
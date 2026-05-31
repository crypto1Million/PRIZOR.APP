from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CallRecording(Base):

    __tablename__ = "call_recordings"

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

    storage_url = Column(
        String
    )

    duration_seconds = Column(
        Integer,
        default=0
    )

    caller_consented = Column(
        Boolean,
        default=False
    )

    receiver_consented = Column(
        Boolean,
        default=False
    )

    recording_enabled = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    call = relationship("VideoCall")
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


class CallParticipant(Base):

    __tablename__ = "call_participants"

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

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    role = Column(
        String,
        default="participant"
    )

    joined_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    left_at = Column(
        DateTime(timezone=True)
    )

    call = relationship("VideoCall")

    user = relationship("User")
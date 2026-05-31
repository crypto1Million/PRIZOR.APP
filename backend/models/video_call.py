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


class VideoCall(Base):

    __tablename__ = "video_calls"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    caller_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    receiver_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    call_type = Column(
        String,
        default="video"
    )

    status = Column(
        String,
        default="ringing"
    )
    # ringing
    # active
    # declined
    # missed
    # ended

    matched_users_only = Column(
        Boolean,
        default=True
    )

    started_at = Column(
        DateTime(timezone=True)
    )

    ended_at = Column(
        DateTime(timezone=True)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    caller = relationship(
        "User",
        foreign_keys=[caller_id]
    )

    receiver = relationship(
        "User",
        foreign_keys=[receiver_id]
    )
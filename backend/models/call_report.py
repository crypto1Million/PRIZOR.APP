from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CallReport(Base):

    __tablename__ = "call_reports"

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

    reporter_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    reported_user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    reason = Column(
        String,
        nullable=False
    )

    description = Column(
        Text
    )

    status = Column(
        String,
        default="open"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    call = relationship("VideoCall")

    reporter = relationship(
        "User",
        foreign_keys=[reporter_id]
    )

    reported_user = relationship(
        "User",
        foreign_keys=[reported_user_id]
    )
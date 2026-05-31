from sqlalchemy import (
    Column, Integer, String,
    Text, DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class StreamReport(Base):

    __tablename__ = "stream_reports"

    id = Column(Integer, primary_key=True, index=True)

    stream_id = Column(
        Integer,
        ForeignKey("live_streams.id")
    )

    reporter_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    reason = Column(String)

    description = Column(Text)

    status = Column(
        String,
        default="open"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    stream = relationship("LiveStream")

    reporter = relationship("User")
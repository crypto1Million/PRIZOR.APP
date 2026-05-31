from sqlalchemy import (
    Column, Integer, DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class StreamViewer(Base):

    __tablename__ = "stream_viewers"

    id = Column(Integer, primary_key=True, index=True)

    stream_id = Column(
        Integer,
        ForeignKey("live_streams.id"),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    joined_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    left_at = Column(
        DateTime(timezone=True)
    )

    stream = relationship("LiveStream")

    user = relationship("User")
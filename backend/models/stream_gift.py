from sqlalchemy import (
    Column, Integer, Float,
    String, DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class StreamGift(Base):

    __tablename__ = "stream_gifts"

    id = Column(Integer, primary_key=True, index=True)

    stream_id = Column(
        Integer,
        ForeignKey("live_streams.id"),
        nullable=False
    )

    sender_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    gift_name = Column(String)

    gift_value = Column(
        Float,
        default=0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    stream = relationship("LiveStream")

    sender = relationship("User")
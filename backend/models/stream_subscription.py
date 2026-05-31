from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class StreamSubscription(Base):

    __tablename__ = "stream_subscriptions"

    id = Column(Integer, primary_key=True, index=True)

    stream_id = Column(
        Integer,
        ForeignKey("live_streams.id")
    )

    subscriber_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    tier = Column(String)

    status = Column(
        String,
        default="active"
    )

    subscribed_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    stream = relationship("LiveStream")

    subscriber = relationship("User")
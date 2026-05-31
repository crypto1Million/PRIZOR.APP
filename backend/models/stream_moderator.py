from sqlalchemy import (
    Column, Integer,
    DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class StreamModerator(Base):

    __tablename__ = "stream_moderators"

    id = Column(Integer, primary_key=True, index=True)

    stream_id = Column(
        Integer,
        ForeignKey("live_streams.id")
    )

    moderator_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    assigned_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    stream = relationship("LiveStream")

    moderator = relationship("User")
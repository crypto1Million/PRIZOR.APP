from sqlalchemy import (
    Column, Integer, Text,
    DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class StreamChatMessage(Base):

    __tablename__ = "stream_chat_messages"

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

    message = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    stream = relationship("LiveStream")

    user = relationship("User")
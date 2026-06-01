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


class SocialConnection(Base):

    __tablename__ = "social_connections"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    connected_user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    connection_type = Column(
        String,
        default="friend"
    )

    connected_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship(
        "User",
        foreign_keys=[user_id]
    )

    connected_user = relationship(
        "User",
        foreign_keys=[connected_user_id]
    )
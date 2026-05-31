from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CreatorEngagement(Base):

    __tablename__ = "creator_engagement"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    likes = Column(
        Integer,
        default=0
    )

    comments = Column(
        Integer,
        default=0
    )

    shares = Column(
        Integer,
        default=0
    )

    saves = Column(
        Integer,
        default=0
    )

    profile_visits = Column(
        Integer,
        default=0
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    creator = relationship(
        "User",
        back_populates="creator_engagement"
    )
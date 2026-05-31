from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text,
    Boolean
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CreatorAchievement(Base):

    __tablename__ = "creator_achievements"

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

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        Text
    )

    category = Column(
        String
    )
    # revenue
    # followers
    # engagement
    # community
    # sponsorship

    milestone_value = Column(
        Integer,
        default=0
    )

    unlocked = Column(
        Boolean,
        default=False
    )

    unlocked_at = Column(
        DateTime(timezone=True)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship(
        "User",
        back_populates="creator_achievements"
    )
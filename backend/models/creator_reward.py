from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    Text,
    Boolean
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CreatorReward(Base):

    __tablename__ = "creator_rewards"

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

    reward_name = Column(
        String,
        nullable=False
    )

    reward_type = Column(
        String
    )
    # cash
    # bonus
    # badge
    # perk
    # sponsorship

    value = Column(
        Float,
        default=0
    )

    description = Column(
        Text
    )

    claimed = Column(
        Boolean,
        default=False
    )

    awarded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship(
        "User",
        back_populates="creator_rewards"
    )
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CreatorXP(Base):

    __tablename__ = "creator_xp"

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

    xp = Column(
        Integer,
        default=0
    )

    level = Column(
        Integer,
        default=1
    )

    lifetime_xp = Column(
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
        back_populates="creator_xp"
    )
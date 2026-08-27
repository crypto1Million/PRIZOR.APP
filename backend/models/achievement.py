from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from backend.db.database import Base


class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(255),
        nullable=False,
        unique=True
    )

    slug = Column(
        String(255),
        nullable=False,
        unique=True
    )

    description = Column(Text)

    icon_url = Column(String(1000))

    badge_color = Column(String(50))

    achievement_type = Column(
        String(100),
        nullable=False
    )

    xp_reward = Column(
        Integer,
        default=0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    users = relationship(
        "UserAchievement",
        back_populates="achievement"
    )
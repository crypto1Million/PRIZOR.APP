from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CommerceAIProfile(Base):

    __tablename__ = "commerce_ai_profiles"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    shopping_score = Column(
        Float,
        default=0
    )

    creator_affinity_score = Column(
        Float,
        default=0
    )

    event_affinity_score = Column(
        Float,
        default=0
    )

    dominant_interest = Column(
        String
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    user = relationship("User")
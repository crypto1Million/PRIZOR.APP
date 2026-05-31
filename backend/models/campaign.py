from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class Campaign(Base):

    __tablename__ = "campaigns"

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

    campaign_type = Column(
        String
    )

    budget = Column(
        Float,
        default=0
    )

    spent = Column(
        Float,
        default=0
    )

    target_url = Column(
        String
    )

    status = Column(
        String,
        default="draft"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    starts_at = Column(
        DateTime(timezone=True)
    )

    ends_at = Column(
        DateTime(timezone=True)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship(
        "User"
    )
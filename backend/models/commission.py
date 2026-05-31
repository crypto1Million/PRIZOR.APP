from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class Commission(Base):

    __tablename__ = "commissions"

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

    commission_type = Column(
        String,
        nullable=False
    )
    # affiliate
    # referral
    # sponsorship
    # marketplace

    amount = Column(
        Float,
        default=0
    )

    percentage = Column(
        Float,
        default=0
    )

    status = Column(
        String,
        default="pending"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User")
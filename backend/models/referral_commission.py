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


class ReferralCommission(Base):

    __tablename__ = "referral_commissions"

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

    referred_user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    referral_code = Column(
        String
    )

    reward_amount = Column(
        Float,
        default=0
    )

    status = Column(
        String,
        default="earned"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship(
        "User",
        foreign_keys=[creator_id]
    )
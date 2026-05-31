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


class AffiliateCommission(Base):

    __tablename__ = "affiliate_commissions"

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

    affiliate_code = Column(
        String,
        nullable=False
    )

    order_reference = Column(
        String
    )

    sale_amount = Column(
        Float,
        default=0
    )

    commission_amount = Column(
        Float,
        default=0
    )

    commission_rate = Column(
        Float,
        default=0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User")
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


class RevenueTransaction(Base):

    __tablename__ = "revenue_transactions"

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

    source_type = Column(
        String,
        nullable=False
    )
    # subscription
    # sponsorship
    # affiliate
    # tips
    # store
    # tickets

    amount = Column(
        Float,
        default=0
    )

    currency = Column(
        String,
        default="USD"
    )

    reference_id = Column(
        String
    )

    status = Column(
        String,
        default="completed"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User") 
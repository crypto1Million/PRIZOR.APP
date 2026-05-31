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


class RevenueStream(Base):

    __tablename__ = "revenue_streams"

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

    stream_name = Column(
        String,
        nullable=False
    )

    stream_type = Column(
        String
    )

    total_revenue = Column(
        Float,
        default=0
    )

    monthly_revenue = Column(
        Float,
        default=0
    )

    yearly_revenue = Column(
        Float,
        default=0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User")
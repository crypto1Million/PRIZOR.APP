from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CreatorMetricsSnapshot(Base):

    __tablename__ = "creator_metrics_snapshots"

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

    followers = Column(
        Integer,
        default=0
    )

    subscribers = Column(
        Integer,
        default=0
    )

    revenue = Column(
        Float,
        default=0
    )

    engagement_score = Column(
        Float,
        default=0
    )

    growth_score = Column(
        Float,
        default=0
    )

    snapshot_date = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship(
        "User",
        back_populates="creator_metric_snapshots"
    )
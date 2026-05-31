from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CreatorView(Base):

    __tablename__ = "creator_views"

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

    viewer_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    source = Column(
        String
    )

    device_type = Column(
        String
    )

    country = Column(
        String
    )

    viewed_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship(
        "User",
        foreign_keys=[creator_id]
    )
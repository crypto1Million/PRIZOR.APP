from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class BusinessNotification(Base):

    __tablename__ = "business_notifications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id"),
        nullable=False
    )

    title = Column(
        String,
        nullable=False
    )

    message = Column(
        Text
    )

    notification_type = Column(
        String
    )

    is_read = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    brand = relationship(
        "BrandProfile"
    )
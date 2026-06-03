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


class EnterpriseSubscription(Base):

    __tablename__ = "enterprise_subscriptions"

    id = Column(Integer, primary_key=True)

    organization_id = Column(
        Integer,
        ForeignKey("enterprise_organizations.id")
    )

    plan = Column(String)

    amount = Column(Float)

    status = Column(
        String,
        default="active"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    organization = relationship(
        "EnterpriseOrganization"
    )
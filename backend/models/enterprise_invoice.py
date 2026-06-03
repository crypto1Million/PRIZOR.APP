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


class EnterpriseInvoice(Base):

    __tablename__ = "enterprise_invoices"

    id = Column(Integer, primary_key=True)

    organization_id = Column(
        Integer,
        ForeignKey("enterprise_organizations.id")
    )

    amount = Column(Float)

    currency = Column(
        String,
        default="USD"
    )

    status = Column(
        String,
        default="pending"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    organization = relationship(
        "EnterpriseOrganization"
    )
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class EnterpriseSupportTicket(Base):

    __tablename__ = "enterprise_support_tickets"

    id = Column(Integer, primary_key=True)

    organization_id = Column(
        Integer,
        ForeignKey("enterprise_organizations.id")
    )

    subject = Column(String)

    description = Column(Text)

    priority = Column(
        String,
        default="normal"
    )

    status = Column(
        String,
        default="open"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    organization = relationship(
        "EnterpriseOrganization"
    )
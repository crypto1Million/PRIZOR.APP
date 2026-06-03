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


class EnterpriseAuditLog(Base):

    __tablename__ = "enterprise_audit_logs"

    id = Column(Integer, primary_key=True)

    organization_id = Column(
        Integer,
        ForeignKey("enterprise_organizations.id")
    )

    action = Column(String)

    details = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    organization = relationship(
        "EnterpriseOrganization"
    )
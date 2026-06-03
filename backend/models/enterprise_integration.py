from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship
from backend.database import Base


class EnterpriseIntegration(Base):

    __tablename__ = "enterprise_integrations"

    id = Column(Integer, primary_key=True)

    organization_id = Column(
        Integer,
        ForeignKey("enterprise_organizations.id")
    )

    provider = Column(String)

    enabled = Column(
        Boolean,
        default=True
    )

    organization = relationship(
        "EnterpriseOrganization"
    )
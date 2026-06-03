from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship
from backend.database import Base


class EnterpriseWorkspace(Base):

    __tablename__ = "enterprise_workspaces"

    id = Column(Integer, primary_key=True)

    organization_id = Column(
        Integer,
        ForeignKey("enterprise_organizations.id")
    )

    name = Column(String)

    organization = relationship(
        "EnterpriseOrganization"
    )
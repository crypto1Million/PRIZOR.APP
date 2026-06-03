from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship
from backend.database import Base


class EnterpriseTeam(Base):

    __tablename__ = "enterprise_teams"

    id = Column(Integer, primary_key=True)

    organization_id = Column(
        Integer,
        ForeignKey("enterprise_organizations.id")
    )

    name = Column(String, nullable=False)

    organization = relationship(
        "EnterpriseOrganization"
    )
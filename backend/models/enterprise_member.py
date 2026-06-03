from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class EnterpriseMember(Base):

    __tablename__ = "enterprise_members"

    id = Column(Integer, primary_key=True)

    organization_id = Column(
        Integer,
        ForeignKey("enterprise_organizations.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    joined_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    organization = relationship(
        "EnterpriseOrganization"
    )

    user = relationship("User")
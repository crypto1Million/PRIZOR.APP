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


class EnterpriseOrganization(Base):

    __tablename__ = "enterprise_organizations"

    id = Column(Integer, primary_key=True)

    account_id = Column(
        Integer,
        ForeignKey("enterprise_accounts.id")
    )

    name = Column(String, nullable=False)

    description = Column(Text)

    website = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    account = relationship("EnterpriseAccount")
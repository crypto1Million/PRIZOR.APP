from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from sqlalchemy.sql import func
from backend.database import Base


class EnterpriseAccount(Base):

    __tablename__ = "enterprise_accounts"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    account_type = Column(
        String,
        default="business"
    )

    active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
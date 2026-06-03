from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship
from backend.database import Base


class EnterprisePermission(Base):

    __tablename__ = "enterprise_permissions"

    id = Column(Integer, primary_key=True)

    role_id = Column(
        Integer,
        ForeignKey("enterprise_roles.id")
    )

    permission_name = Column(String)

    role = relationship(
        "EnterpriseRole"
    )
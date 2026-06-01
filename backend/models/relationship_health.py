from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class RelationshipHealth(Base):

    __tablename__ = "relationship_health"

    id = Column(Integer, primary_key=True, index=True)

    user_one_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user_two_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    health_score = Column(
        Float,
        default=0
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user_one = relationship(
        "User",
        foreign_keys=[user_one_id]
    )

    user_two = relationship(
        "User",
        foreign_keys=[user_two_id]
    )
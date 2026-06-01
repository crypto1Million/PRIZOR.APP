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


class RelationshipEvent(Base):

    __tablename__ = "relationship_events"

    id = Column(Integer, primary_key=True, index=True)

    user_one_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user_two_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    event_type = Column(String)

    event_description = Column(Text)

    occurred_at = Column(
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
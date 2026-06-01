from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from backend.database import Base


class CreatorAffinity(Base):

    __tablename__ = "creator_affinities"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    affinity_score = Column(
        Float,
        default=0
    )

    user = relationship(
        "User",
        foreign_keys=[user_id]
    )

    creator = relationship(
        "User",
        foreign_keys=[creator_id]
    )
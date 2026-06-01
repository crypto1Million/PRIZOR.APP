from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from backend.database import Base


class ProductAffinity(Base):

    __tablename__ = "product_affinities"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    affinity_score = Column(
        Float,
        default=0
    )

    user = relationship("User")
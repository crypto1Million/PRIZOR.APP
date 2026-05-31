from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey, Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class SponsorshipContract(Base):

    __tablename__ = "sponsorship_contracts"

    id = Column(Integer, primary_key=True, index=True)

    sponsorship_id = Column(
        Integer,
        ForeignKey("sponsorships.id"),
        nullable=False
    )

    contract_title = Column(String)

    contract_url = Column(String)

    terms = Column(Text)

    signed_by_creator = Column(String)

    signed_by_brand = Column(String)

    signed_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    sponsorship = relationship("Sponsorship")
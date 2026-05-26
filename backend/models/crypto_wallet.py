from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base

class CryptoWallet(Base):
    __tablename__ = "crypto_wallets"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    wallet_address = Column(String, unique=True)

    wallet_type = Column(String)

    is_primary = Column(Integer, default=1)
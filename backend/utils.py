# utils.py

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 🔐 Hash password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# 🔐 Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# 🧠 Normalize text (useful for matching later)
def normalize_text(text: str) -> str:
    if not text:
        return ""
    return text.lower().strip()
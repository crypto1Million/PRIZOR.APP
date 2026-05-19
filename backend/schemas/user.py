from pydantic import BaseModel, EmailStr
from pydantic import Field
from datetime import datetime

password: str = Field(min_length=6)

# ==============================
# CREATE USER
# ==============================
class UserCreate(BaseModel):
    username: str
    email: EmailStr   # ✅ ADD THIS
    password: str

# ==============================
# LOGIN
# ==============================
class UserLogin(BaseModel):
    email: EmailStr
    password: str    

# ==============================
# OUTPUT (SAFE RESPONSE)
# ==============================
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr   # ✅ ADD THIS

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    age: int
    location: str
    gender: str
    preference: str

class UserResponse(BaseModel):

    id: int
    username: str
    bio: str | None

    is_online: bool
    last_seen: datetime | None

    class Config:
        orm_mode = True

        
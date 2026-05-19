from pydantic import BaseModel

class SwipeCreate(BaseModel):
    to_user: str
    action: str

class SwipeCreate(BaseModel):
    swiped_id: str
    is_like: bool

class SwipeCreate(BaseModel):
    swiped_user_id: int
    liked: bool
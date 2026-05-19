from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend import models
from backend.auth import get_current_user

router = APIRouter(prefix="/block", tags=["Block"])


@router.post("/{user_id}")

def block_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    existing = db.query(models.Block).filter(
        models.Block.blocker_id == current_user.id,
        models.Block.blocked_id == user_id
    ).first()

    if existing:
        return {"message": "Already blocked"}

    block = models.Block(
        blocker_id=current_user.id,
        blocked_id=user_id
    )

    db.add(block)

    db.commit()

    return {"message": "User blocked"}
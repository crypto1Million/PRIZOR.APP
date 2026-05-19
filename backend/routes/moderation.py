from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models

from backend.database import get_db
from routes.auth import get_current_user

router = APIRouter(
    prefix="/moderation",
    tags=["Moderation"]
)


@router.post("/report")
def report_user(
    reported_user_id: int,
    reason: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    report = models.Report(
        reporter_id=current_user,
        reported_user_id=reported_user_id,
        reason=reason
    )

    db.add(report)

    db.commit()

    return {
        "message": "User reported"
    }

@router.post("/block")
def block_user(
    blocked_user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    exists = db.query(models.Block).filter(
        models.Block.blocker_id == current_user,
        models.Block.blocked_user_id == blocked_user_id
    ).first()

    if exists:
        return {"message": "Already blocked"}

    block = models.Block(
        blocker_id=current_user,
        blocked_user_id=blocked_user_id
    )

    db.add(block)

    db.commit()

    return {"message": "User blocked"}    
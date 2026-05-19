from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas

from backend.database import get_db
from routes.auth import get_current_user

from core.trust import calculate_trust

router = APIRouter(
    prefix="/report",
    tags=["Reports"]
)

@router.post("/")
def report_user(
    report: schemas.ReportCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    target_user = db.query(models.User).filter(
        models.User.id == report.user_id
    ).first()

    if not target_user:
        return {"error": "User not found"}

    # Prevent self-report abuse
    if target_user.id == current_user:
        return {"error": "Cannot report yourself"}

    # Save report
    new_report = models.Report(
        reporter_id=current_user,
        reported_user_id=report.user_id,
        reason=report.reason
    )

    db.add(new_report)

    # Increase report count
    target_user.report_count += 1

    # Recalculate trust score
    target_user.trust_score = calculate_trust(target_user)

    db.commit()

    return {
        "message": "User reported successfully"
    }
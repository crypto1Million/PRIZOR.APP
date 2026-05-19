from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend import models
from backend.auth import get_current_user

router = APIRouter()


def calculate_discovery_score(user):

    like_ratio = min(user.like_ratio or 0, 1)
    activity_score = min(user.activity_score or 0, 1)

    elo_score = min((user.elo_score or 0) / 1000, 2)

    exposure_penalty = max(user.exposure_penalty or 1, 0.2)

    match_boost = user.match_boost or 1
    boost = user.boost_multiplier or 1

    score = (
        (like_ratio * 0.3) +
        (activity_score * 0.2) +
        (elo_score * 0.5)
    )

    return score * exposure_penalty * match_boost * boost


@router.get("/feed")
def get_discovery_feed(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    blocked_users = db.query(models.Block.blocked_id).filter(
        models.Block.blocker_id == current_user.id
    )

    blocked_by_users = db.query(models.Block.blocker_id).filter(
        models.Block.blocked_id == current_user.id
    )

    swiped_users = db.query(models.Swipe.swiped_id).filter(
        models.Swipe.swiper_id == current_user.id
    )

    candidate_users = db.query(models.User).filter(
        models.User.id != current_user.id,

        ~models.User.id.in_(blocked_users),

        ~models.User.id.in_(blocked_by_users),

        ~models.User.id.in_(swiped_users)
    ).all()

    ranked_users = sorted(
        candidate_users,
        key=lambda x: calculate_discovery_score(x),
        reverse=True
    )

    return ranked_users[:20]
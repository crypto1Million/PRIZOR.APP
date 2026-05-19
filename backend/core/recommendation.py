from backend.core.redis import redis_client
from backend.database import SessionLocal
from backend import models
from datetime import datetime, timedelta
from sqlalchemy import and_
from sqlalchemy.orm import Session
from backend.core.image_moderation import check_image_safe
from backend.core.limiter import limiter
from fastapi import Request
import random
import time
import json

def calculate_recommendation_score(current, target):


    score = 0

    # ==============================
    # 🎯 ELO SIMILARITY
    # ==============================
    elo_diff = abs(current.elo_score - target.elo_score)

    if elo_diff < 100:
        score += 30

    elif elo_diff < 300:
        score += 15

    # ==============================
    # ⚡ ACTIVITY
    # ==============================
    score += min(target.activity_score, 50)

    # ==============================
    # 🖼 PROFILE QUALITY
    # ==============================
    score += target.profile_completion

    # ==============================
    # 🚀 BOOST USERS
    # ==============================
    if target.boost_active:
        score += 100

    # ==============================
    # 🎯 INTEREST MATCH
    # ==============================
    if current.interests and target.interests:

        current_interests = set(
            current.interests.lower().split(",")
        )

        target_interests = set(
            target.interests.lower().split(",")
        )

        common = current_interests.intersection(
            target_interests
        )

        score += len(common) * 20

    return score

def get_recommendations_for_user(db: Session, user_id: int):    

    current_user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if not current_user:
        return []

    candidates = db.query(models.User).filter(
        and_(
            models.User.id != user_id,
            models.User
            .last_active > datetime.utcnow() - timedelta(days=30)
        )
        ).all()
    scored_candidates = []
    for candidate in candidates:
        score = calculate_recommendation_score(current_user, candidate)
        scored_candidates.append((candidate, score))

    scored_candidates.sort(key=lambda x: x[1], reverse=True)
    return [candidate for candidate, score in scored_candidates]

def get_ranked_feed(user_id, candidate_users):

    cached_feed = redis_client.get(f"user:{user_id}:feed")
    if cached_feed:
        return json.loads(cached_feed)
    ranked_feed = sorted(
        candidate_users,
        key=lambda u: calculate_recommendation_score(
            current_user,
            u
        ),
        reverse=True
    )
    redis_client.set(
        f"user:{user_id}:feed",
        json.dumps([u.id for u in ranked_feed]),
        ex=300
    )

    return ranked_feed

    


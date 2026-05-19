from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from database import SessionLocal
import models

scheduler = BackgroundScheduler()


# ==============================
# 🚀 EXPIRE BOOSTS
# ==============================
def expire_boosts():

    db = SessionLocal()

    try:

        users = db.query(models.User).filter(
            models.User.boost_active == True
        ).all()

        now = datetime.utcnow()

        for user in users:

            if user.boost_expires_at:

                if user.boost_expires_at < now:

                    user.boost_active = False
                    user.boost_multiplier = 1

        db.commit()

    finally:
        db.close()


# ==============================
# 🧹 CLEAN INACTIVE USERS
# ==============================
def cleanup_inactive_users():

    db = SessionLocal()

    try:

        users = db.query(models.User).all()

        now = datetime.utcnow()

        for user in users:

            if user.last_active:

                days = (now - user.last_active).days

                if days > 30:

                    user.activity_score = 0

        db.commit()

    finally:
        db.close()


# ==============================
# ⏰ JOBS
# ==============================
scheduler.add_job(
    expire_boosts,
    "interval",
    minutes=5
)

scheduler.add_job(
    cleanup_inactive_users,
    "interval",
    hours=12
)
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from backend.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    age = Column(Integer)
    location = Column(String)
    gender = Column(String)
    preference = Column(String)
    likes_received = Column(Integer, default=0)
    swipes_done = Column(Integer, default=0)
    last_active = Column(DateTime)
    elo_score = Column(Integer, default=1000)
    last_swipe_time = Column(DateTime)
    swipes_today = Column(Integer, default=0)
    last_swipe_reset = Column(DateTime)
    boost_active = Column(Boolean, default=False)
    boost_expires_at = Column(DateTime)
    boost_multiplier = Column(Integer, default=1)  # 1 = normal, 2x, 3x etc
    last_seen = Column(DateTime, nullable=True)
    is_online = Column(Boolean, default=False)
    profile_image = Column(String, nullable=True)
    activity_score = Column(Integer, default=0)
    profile_completeness = Column(Integer, default=0)
    discover_score = Column(Integer, default=0)
    preferred_gender = Column(String, nullable=True)
    preferred_age_min = Column(Integer, default=18)
    preferred_age_max = Column(Integer, default=40)
    interests = Column(String, nullable=True)
    fcm_token = Column(String, nullable=True)
    trust_score = Column(Integer, default=50)
    is_verified = Column(Boolean, default=False)
    warning_count = Column(Integer, default=0)
    is_shadow_banned = Column(Boolean, default=False)
    report_count = Column(Integer, default=0)
    warning_count = Column(Integer, default=0)
    trust_score = Column(Integer, default=100)
    verification_token = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
    reset_token_expiry = Column(DateTime, nullable=True)
    pronouns = Column(String)
    identity_tags = Column(String)
    verified_identity = Column(Boolean, default=False)
    creator_memberships = relationship(
        "CreatorMembership",
        back_populates="creator"
    )

    creator_badges = relationship(
        "CreatorBadge",
        back_populates="creator"
    )

    creator_rewards = relationship(
        "CreatorReward",
        back_populates="creator"
    )

    creator_xp = relationship(
        "CreatorXP",
        back_populates="creator",
        uselist=False
    )

    creator_achievements = relationship(
        "CreatorAchievement",
        back_populates="creator"
    )

    creator_analytics_events = relationship(
    "CreatorAnalyticsEvent",
    back_populates="creator"
    )

    creator_engagement = relationship(
    "CreatorEngagement",
    back_populates="creator",
    uselist=False
    )

    creator_metric_snapshots = relationship(
        "CreatorMetricsSnapshot",
        back_populates="creator"
    )

    creator_revenue_analytics = relationship(
        "CreatorRevenueAnalytics",
        back_populates="creator"
    )

    revenue_transactions = relationship("RevenueTransaction")
    revenue_streams = relationship("RevenueStream")
    revenue_reports = relationship("RevenueReport")
    revenue_payouts = relationship("RevenuePayout")
    revenue_snapshots = relationship("RevenueSnapshot")

    commissions = relationship("Commission")

    affiliate_commissions = relationship("AffiliateCommission")

    referral_commissions = relationship(
       "ReferralCommission",
       foreign_keys="ReferralCommission.creator_id"
    )

    commission_reports = relationship("CommissionReport")


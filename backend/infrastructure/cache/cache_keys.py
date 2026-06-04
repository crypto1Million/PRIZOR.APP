class CacheKeys:

    @staticmethod
    def user_profile(user_id: int):
        return f"user:profile:{user_id}"

    @staticmethod
    def user_session(user_id: int):
        return f"user:session:{user_id}"

    @staticmethod
    def creator_feed(user_id: int):
        return f"feed:creator:{user_id}"

    @staticmethod
    def recommendation_feed(user_id: int):
        return f"feed:recommendation:{user_id}"

    @staticmethod
    def analytics_daily(date: str):
        return f"analytics:daily:{date}"

    @staticmethod
    def rate_limit(identifier: str):
        return f"ratelimit:{identifier}"
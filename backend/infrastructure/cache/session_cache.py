from .cache_manager import cache_manager
from .cache_keys import CacheKeys


class SessionCache:

    SESSION_TTL = 86400 * 30

    async def store_session(
        self,
        user_id: int,
        session_data: dict
    ):

        await cache_manager.set(
            CacheKeys.user_session(user_id),
            session_data,
            self.SESSION_TTL
        )

    async def get_session(
        self,
        user_id: int
    ):

        return await cache_manager.get(
            CacheKeys.user_session(user_id)
        )

    async def revoke_session(
        self,
        user_id: int
    ):

        await cache_manager.delete(
            CacheKeys.user_session(user_id)
        )


session_cache = SessionCache()
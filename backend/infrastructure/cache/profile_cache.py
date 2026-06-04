from .cache_manager import cache_manager
from .cache_keys import CacheKeys


class ProfileCache:

    PROFILE_TTL = 3600

    async def cache_profile(
        self,
        user_id: int,
        profile: dict
    ):

        await cache_manager.set(
            CacheKeys.user_profile(user_id),
            profile,
            self.PROFILE_TTL
        )

    async def get_profile(
        self,
        user_id: int
    ):

        return await cache_manager.get(
            CacheKeys.user_profile(user_id)
        )

    async def invalidate(
        self,
        user_id: int
    ):

        await cache_manager.delete(
            CacheKeys.user_profile(user_id)
        )


profile_cache = ProfileCache()
from .cache_manager import cache_manager
from .cache_keys import CacheKeys


class FeedCache:

    FEED_TTL = 900

    async def cache_feed(
        self,
        user_id: int,
        feed_data: list
    ):

        await cache_manager.set(
            CacheKeys.recommendation_feed(user_id),
            feed_data,
            self.FEED_TTL
        )

    async def get_feed(
        self,
        user_id: int
    ):

        return await cache_manager.get(
            CacheKeys.recommendation_feed(user_id)
        )

    async def invalidate_feed(
        self,
        user_id: int
    ):

        await cache_manager.delete(
            CacheKeys.recommendation_feed(user_id)
        )


feed_cache = FeedCache()
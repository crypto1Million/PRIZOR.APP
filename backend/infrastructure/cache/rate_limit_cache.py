from .redis_client import redis_client
from .cache_keys import CacheKeys


class RateLimitCache:

    async def increment(
        self,
        identifier: str,
        ttl: int = 60
    ):

        redis = redis_client.get_client()

        key = CacheKeys.rate_limit(identifier)

        count = await redis.incr(key)

        if count == 1:
            await redis.expire(key, ttl)

        return count

    async def get(
        self,
        identifier: str
    ):

        redis = redis_client.get_client()

        key = CacheKeys.rate_limit(identifier)

        value = await redis.get(key)

        return int(value or 0)

    async def reset(
        self,
        identifier: str
    ):

        redis = redis_client.get_client()

        await redis.delete(
            CacheKeys.rate_limit(identifier)
        )


rate_limit_cache = RateLimitCache()
import json

from .redis_client import redis_client


class CacheManager:

    DEFAULT_TTL = 3600

    async def get(self, key: str):

        redis = redis_client.get_client()

        value = await redis.get(key)

        if not value:
            return None

        return json.loads(value)

    async def set(
        self,
        key: str,
        value,
        ttl: int = DEFAULT_TTL
    ):

        redis = redis_client.get_client()

        await redis.set(
            key,
            json.dumps(value),
            ex=ttl
        )

    async def delete(self, key: str):

        redis = redis_client.get_client()

        await redis.delete(key)

    async def exists(self, key: str):

        redis = redis_client.get_client()

        return await redis.exists(key)


cache_manager = CacheManager()
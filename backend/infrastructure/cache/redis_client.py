from redis.asyncio import Redis
from backend.config import settings


class RedisClient:

    _client = None

    @classmethod
    def get_client(cls) -> Redis:

        if cls._client is None:

            cls._client = Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                password=settings.REDIS_PASSWORD,
                decode_responses=True
            )

        return cls._client

    @classmethod
    async def close(cls):

        if cls._client:
            await cls._client.close()


redis_client = RedisClient()
from datetime import date

from .cache_manager import cache_manager
from .cache_keys import CacheKeys


class AnalyticsCache:

    ANALYTICS_TTL = 1800

    async def cache_daily_metrics(
        self,
        metrics: dict
    ):

        key = CacheKeys.analytics_daily(
            str(date.today())
        )

        await cache_manager.set(
            key,
            metrics,
            self.ANALYTICS_TTL
        )

    async def get_daily_metrics(self):

        key = CacheKeys.analytics_daily(
            str(date.today())
        )

        return await cache_manager.get(key)


analytics_cache = AnalyticsCache()
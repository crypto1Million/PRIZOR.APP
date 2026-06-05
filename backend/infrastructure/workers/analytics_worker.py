from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def aggregate_analytics():

    logger.info(
        "Running analytics aggregation"
    )

    return {
        "success": True
    }
from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def moderate_content(
    content_id: int,
    content_type: str
):

    logger.info(
        f"Moderating {content_type} {content_id}"
    )

    return {
        "content_id": content_id,
        "safe": True
    }
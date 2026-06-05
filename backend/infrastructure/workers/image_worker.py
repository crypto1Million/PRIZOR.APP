from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def optimize_image(
    image_id: int
):

    logger.info(
        f"Optimizing image {image_id}"
    )

    return {
        "image_id": image_id,
        "optimized": True
    }
from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def process_stream_recording(
    stream_id: int
):

    logger.info(
        f"Processing stream {stream_id}"
    )

    return {
        "stream_id": stream_id,
        "processed": True
    }
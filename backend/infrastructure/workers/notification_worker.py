from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    max_retries=3
)
def send_notification_task(
    self,
    user_id: int,
    title: str,
    message: str
):
    try:

        logger.info(
            f"Sending notification to {user_id}"
        )

        # Push notification integration

        return {
            "success": True,
            "user_id": user_id
        }

    except Exception as e:

        raise self.retry(
            exc=e,
            countdown=30
        )
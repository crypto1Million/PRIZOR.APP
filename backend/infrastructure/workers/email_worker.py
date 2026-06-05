from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    max_retries=3
)
def send_email_task(
    self,
    recipient: str,
    subject: str,
    body: str
):
    try:

        logger.info(
            f"Sending email to {recipient}"
        )

        # Integrate SendGrid / SES later

        return {
            "success": True,
            "recipient": recipient
        }

    except Exception as e:

        raise self.retry(
            exc=e,
            countdown=60
        )
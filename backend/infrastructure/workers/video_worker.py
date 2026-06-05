from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def transcode_video(
    video_id: int
):

    logger.info(
        f"Transcoding video {video_id}"
    )

    # ffmpeg integration later

    return {
        "video_id": video_id,
        "status": "completed"
    }
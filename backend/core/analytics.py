from backend import models

def track_event(
    db,
    user_id,
    event_type,
    metadata=None
):

    event = models.AnalyticsEvent(
        user_id=user_id,
        event_type=event_type,
        event_metadata=metadata
    )

    db.add(event)

    db.commit()
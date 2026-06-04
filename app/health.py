from fastapi import APIRouter
from app.ingestion import EVENT_STORE
from datetime import datetime

router = APIRouter()


@router.get("/health")
def health_check():

    total_events = len(EVENT_STORE)

    latest_timestamp = None

    if total_events > 0:

        timestamps = []

        for event in EVENT_STORE:
            try:
                timestamps.append(
                    datetime.fromisoformat(
                        event.timestamp
                    )
                )
            except:
                pass

        if timestamps:
            latest_timestamp = max(timestamps)

    feed_status = "HEALTHY"

    if latest_timestamp:

        minutes_since_event = (
            datetime.now()
            - latest_timestamp
        ).total_seconds() / 60

        if minutes_since_event > 10:
            feed_status = "STALE_FEED"

    return {
        "status": "UP",
        "events_loaded": total_events,
        "latest_event_timestamp":
            str(latest_timestamp)
            if latest_timestamp
            else None,
        "feed_status": feed_status
    }
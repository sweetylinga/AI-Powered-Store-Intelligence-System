from fastapi import APIRouter
from app.ingestion import EVENT_STORE

router = APIRouter()


@router.get("/stores/{store_id}/metrics")
def get_store_metrics(store_id: str):

    # Filter events for store
    store_events = [
        event
        for event in EVENT_STORE
        if event.store_id == store_id
        and not event.is_staff
    ]

    # Unique visitors
    unique_visitors = len(
        set(event.visitor_id for event in store_events)
    )

    # Queue events
    queue_events = [
        event
        for event in store_events
        if event.event_type == "BILLING_QUEUE_JOIN"
    ]

    queue_depth = len(queue_events)

    # Abandoned queue
    abandoned_events = [
        event
        for event in store_events
        if event.event_type == "BILLING_QUEUE_ABANDON"
    ]

    abandonment_rate = 0

    if queue_depth > 0:
        abandonment_rate = round(
            (len(abandoned_events) / queue_depth) * 100,
            2
        )

    # Conversion rate
    converted_visitors = set(
        event.visitor_id
        for event in queue_events
    )

    abandoned_visitors = set(
        event.visitor_id
        for event in abandoned_events
    )

    successful_visitors = (
        converted_visitors - abandoned_visitors
    )

    conversion_rate = 0

    if unique_visitors > 0:
        conversion_rate = round(
            (
                len(successful_visitors)
                / unique_visitors
            ) * 100,
            2
        )

    # Average dwell per zone
    zone_times = {}

    for event in store_events:

        if (
            event.event_type == "ZONE_DWELL"
            and event.zone_name
            and event.wait_seconds is not None
        ):

            zone = event.zone_name

            if zone not in zone_times:
                zone_times[zone] = []

            zone_times[zone].append(
                event.wait_seconds
            )

    avg_dwell_per_zone = {}

    for zone, times in zone_times.items():
        avg_dwell_per_zone[zone] = round(
            sum(times) / len(times),
            2
        )

    return {
        "store_id": store_id,
        "unique_visitors": unique_visitors,
        "conversion_rate": conversion_rate,
        "avg_dwell_per_zone": avg_dwell_per_zone,
        "queue_depth": queue_depth,
        "abandonment_rate": abandonment_rate
    }
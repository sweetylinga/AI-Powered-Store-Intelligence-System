from fastapi import APIRouter
from app.ingestion import EVENT_STORE

router = APIRouter()


@router.get("/stores/{store_id}/funnel")
def get_funnel(store_id: str):

    store_events = [
        event
        for event in EVENT_STORE
        if event.store_id == store_id
        and not event.is_staff
    ]

    visitors = set(
        event.visitor_id
        for event in store_events
    )

    total_entries = len(visitors)

    zone_visitors = set(
        event.visitor_id
        for event in store_events
        if event.event_type == "ZONE_DWELL"
    )

    billing_visitors = set(
        event.visitor_id
        for event in store_events
        if event.event_type == "BILLING_QUEUE_JOIN"
    )

    abandoned_visitors = set(
        event.visitor_id
        for event in store_events
        if event.event_type == "BILLING_QUEUE_ABANDON"
    )

    purchased_visitors = (
        billing_visitors - abandoned_visitors
    )

    return {
        "store_id": store_id,
        "funnel": {
            "entry": total_entries,
            "zone_visit": len(zone_visitors),
            "billing_queue": len(billing_visitors),
            "purchase": len(purchased_visitors)
        }
    }
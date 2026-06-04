from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# In-memory storage for events
EVENT_STORE = []


class StoreEvent(BaseModel):
    store_id: str
    visitor_id: str
    timestamp: str
    event_type: str

    is_staff: Optional[bool] = False

    zone_id: Optional[str] = None
    zone_name: Optional[str] = None
    zone_type: Optional[str] = None

    wait_seconds: Optional[int] = None
    abandoned: Optional[bool] = False


@router.post("/events/ingest")
def ingest_events(events: List[StoreEvent]):

    EVENT_STORE.extend(events)

    return {
        "message": "Events ingested successfully",
        "events_received": len(events)
    }
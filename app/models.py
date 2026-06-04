from pydantic import BaseModel
from typing import Optional


class StoreEvent(BaseModel):
    event_type: str

    id_token: Optional[str] = None
    track_id: Optional[int] = None

    store_code: Optional[str] = None
    store_id: Optional[str] = None

    camera_id: str

    event_timestamp: Optional[str] = None
    event_time: Optional[str] = None

    is_staff: Optional[bool] = False

    gender_pred: Optional[str] = None
    gender: Optional[str] = None

    age_pred: Optional[int] = None
    age: Optional[int] = None

    age_bucket: Optional[str] = None

    zone_id: Optional[str] = None
    zone_name: Optional[str] = None
    zone_type: Optional[str] = None

    wait_seconds: Optional[int] = None
    abandoned: Optional[bool] = None
    queue_position_at_join: Optional[int] = None
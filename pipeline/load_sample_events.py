import requests

BASE_URL = "http://127.0.0.1:8000"

events = [
    {
        "store_id": "store_1076",
        "visitor_id": "visitor_1",
        "timestamp": "2026-03-08T10:00:00",
        "event_type": "ZONE_DWELL",
        "zone_name": "Entrance",
        "wait_seconds": 20,
        "is_staff": False
    },
    {
        "store_id": "store_1076",
        "visitor_id": "visitor_1",
        "timestamp": "2026-03-08T10:02:00",
        "event_type": "BILLING_QUEUE_JOIN",
        "wait_seconds": 30,
        "is_staff": False
    },
    {
        "store_id": "store_1076",
        "visitor_id": "visitor_2",
        "timestamp": "2026-03-08T10:04:00",
        "event_type": "ZONE_DWELL",
        "zone_name": "Electronics",
        "wait_seconds": 40,
        "is_staff": False
    },
    {
        "store_id": "store_1076",
        "visitor_id": "visitor_2",
        "timestamp": "2026-03-08T10:05:00",
        "event_type": "BILLING_QUEUE_JOIN",
        "wait_seconds": 25,
        "is_staff": False
    },
    {
        "store_id": "store_1076",
        "visitor_id": "visitor_2",
        "timestamp": "2026-03-08T10:06:00",
        "event_type": "BILLING_QUEUE_ABANDON",
        "wait_seconds": 25,
        "is_staff": False
    },
    {
        "store_id": "store_1076",
        "visitor_id": "visitor_3",
        "timestamp": "2026-03-08T10:07:00",
        "event_type": "ZONE_DWELL",
        "zone_name": "Groceries",
        "wait_seconds": 26,
        "is_staff": False
    },
    {
        "store_id": "store_1076",
        "visitor_id": "visitor_3",
        "timestamp": "2026-03-08T10:09:00",
        "event_type": "BILLING_QUEUE_JOIN",
        "wait_seconds": 31,
        "is_staff": False
    }
]

response = requests.post(
    f"{BASE_URL}/events/ingest",
    json=events
)

print(response.json())
print(f"Loaded {len(events)} events")
{
    "store_id": "store_1076",
    "visitor_id": "visitor_4",
    "timestamp": "2026-03-08T10:10:00",
    "event_type": "BILLING_QUEUE_JOIN",
    "is_staff": False
},
{
    "store_id": "store_1076",
    "visitor_id": "visitor_5",
    "timestamp": "2026-03-08T10:11:00",
    "event_type": "BILLING_QUEUE_JOIN",
    "is_staff": False
},
{
    "store_id": "store_1076",
    "visitor_id": "visitor_6",
    "timestamp": "2026-03-08T10:12:00",
    "event_type": "BILLING_QUEUE_JOIN",
    "is_staff": False
}
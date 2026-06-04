from ultralytics import YOLO
import cv2
import time
import requests
from datetime import datetime
from threading import Lock

cv2.setNumThreads(0)

# Load YOLO model
model = YOLO("yolov8n.pt")

# CCTV video paths
video_paths = {
    "entry": "data/videos/entry_1.mp4.mp4",
    "billing": "data/videos/billing_area.mp4.mp4",
    "zone": "data/videos/zone.mp4.mp4"
}

# Open videos
# Prevent parallel video access crashes
video_lock = Lock()

# Open videos
caps = {
    key: cv2.VideoCapture(path)
    for key, path in video_paths.items()
}
print("ENTRY OPEN:", caps["entry"].isOpened())
print("BILLING OPEN:", caps["billing"].isOpened())
print("ZONE OPEN:", caps["zone"].isOpened())
# Live dashboard state
live_state = {
    "visitors": 0,
    "queue_depth": 0,
    "high_attention_zone": "Electronics",
    "dwell_time": 0,
    "events": []
}


def detect_people(frame):
   results = model( frame, verbose=False, stream=False, device="cpu",workers=0)
   person_count = 0
   for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            # person class = 0
            if cls == 0 and conf > 0.05:
                person_count += 1
        return person_count


def store_event(visitor_id, event_type, zone_name=None):
    try:
        payload = [
            {
                "store_id": "store_1076",
                "visitor_id": visitor_id,
                "timestamp": datetime.now().isoformat(),
                "event_type": event_type,
                "zone_name": zone_name
            }
        ]

        requests.post(
            "http://127.0.0.1:8000/events/ingest",
            json=payload,
            timeout=3
        )

    except Exception as e:
        print("Event store error:", e)


def update_tracking():
    entry_cap = caps["entry"]
    billing_cap = caps["billing"]
    zone_cap = caps["zone"]

    ret1, frame1 = entry_cap.read()
    ret2, frame2 = billing_cap.read()
    ret3, frame3 = zone_cap.read()

    # DEBUG
    print("ENTRY FRAME:", ret1)
    print("BILLING FRAME:", ret2)
    print("ZONE FRAME:", ret3)

    # Restart videos automatically
    if not ret1:
        entry_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret1, frame1 = entry_cap.read()

    if not ret2:
        billing_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret2, frame2 = billing_cap.read()

    if not ret3:
        zone_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret3, frame3 = zone_cap.read()

    # Detect people
    visitors = detect_people(frame1)
    queue_depth = detect_people(frame2)
    zone_people = detect_people(frame3)

    # DEBUG
    print("Visitors:", visitors)
    print("Queue:", queue_depth)
    print("Zone:", zone_people)

    # Update metrics
    live_state["visitors"] = visitors
    live_state["queue_depth"] = queue_depth

    # Dwell time
    if zone_people > 0:
        live_state["dwell_time"] += 2

    timestamp = time.strftime("%I:%M:%S %p")

    events = []

    # ENTRY EVENTS
    if visitors > 0:
        events.append({
            "time": timestamp,
            "event": f"{visitors} visitor(s) detected at entrance",
            "source": "entry_1.mp4"
        })

        store_event(
            visitor_id=f"visitor_{visitors}",
            event_type="ENTRY_DETECTED",
            zone_name="Entrance"
        )

    # BILLING EVENTS
    if queue_depth > 0:
        events.append({
            "time": timestamp,
            "event": f"Queue depth detected: {queue_depth}",
            "source": "billing_area.mp4"
        })

        store_event(
            visitor_id="queue_customer",
            event_type="QUEUE_DETECTED",
            zone_name="Billing"
        )

    # ZONE EVENTS
    if zone_people > 0:
        events.append({
            "time": timestamp,
            "event": "Electronics zone activity detected",
            "source": "zone.mp4"
        })

        store_event(
            visitor_id="zone_customer",
            event_type="ZONE_ACTIVITY",
            zone_name="Electronics"
        )

    live_state["events"] = events

    return live_state
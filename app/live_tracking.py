from ultralytics import YOLO
import cv2
import time
from threading import Lock

cv2.setNumThreads(0)

# Load YOLO once
model = YOLO("yolov8n.pt")

# CCTV video paths
video_paths = {
    "entry": "data/videos/entry_1.mp4.mp4",
    "billing": "data/videos/billing_area.mp4.mp4",
    "zone": "data/videos/zone.mp4.mp4"
}

video_lock = Lock()

# Open videos
caps = {
    key: cv2.VideoCapture(path)
    for key, path in video_paths.items()
}

print("ENTRY OPEN:", caps["entry"].isOpened())
print("BILLING OPEN:", caps["billing"].isOpened())
print("ZONE OPEN:", caps["zone"].isOpened())


live_state = {
    "visitors": 0,
    "queue_depth": 0,
    "high_attention_zone": "Electronics",
    "dwell_time": 0,
    "events": []
}


def detect_people(frame):
    results = model(
        frame,
        verbose=False,
        stream=False,
        device="cpu"
    )

    count = 0

    for result in results:
        for box in result.boxes:
            if int(box.cls[0]) == 0 and float(box.conf[0]) > 0.05:
                count += 1

    return count


def reopen_if_needed(key):
    global caps

    if not caps[key].isOpened():
        print(f"Reopening {key} video...")
        caps[key].release()
        caps[key] = cv2.VideoCapture(video_paths[key])


def read_frame(key):
    reopen_if_needed(key)

    cap = caps[key]

    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()

    return frame


def update_tracking():

    with video_lock:

        try:

            frame1 = read_frame("entry")
            frame2 = read_frame("billing")
            frame3 = read_frame("zone")

            if frame1 is None or frame2 is None or frame3 is None:
                return live_state

            visitors = detect_people(frame1)
            queue_depth = detect_people(frame2)
            zone_people = detect_people(frame3)

            live_state["visitors"] = visitors
            live_state["queue_depth"] = queue_depth

            if zone_people > 0:
                live_state["dwell_time"] += 2
            else:
                live_state["dwell_time"] = 0

            timestamp = time.strftime("%I:%M:%S %p")

            events = []

            if visitors > 0:
                events.append({
                    "time": timestamp,
                    "event": f"{visitors} visitor(s) detected at entrance",
                    "source": "entry_1.mp4"
                })

            if queue_depth > 0:
                events.append({
                    "time": timestamp,
                    "event": f"Queue depth detected: {queue_depth}",
                    "source": "billing_area.mp4"
                })

            if zone_people > 0:
                events.append({
                    "time": timestamp,
                    "event": "Electronics zone activity detected",
                    "source": "zone.mp4"
                })

            live_state["events"] = events

            return live_state

        except Exception as e:

            print("Live tracking error:", e)

            return live_state

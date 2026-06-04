# DESIGN CHOICES

## Model Selection

### YOLOv8

Chosen because:

* Fast inference speed
* Strong person detection accuracy
* Lightweight deployment
* Easy OpenCV integration

Alternative models considered:

* Faster R-CNN
* SSD MobileNet

YOLOv8 provided the best balance between accuracy and performance.

## Framework Selection

### FastAPI

Chosen because:

* Automatic Swagger documentation
* High performance
* Type validation
* Easy REST API development

### React

Chosen because:

* Component-based architecture
* Fast dashboard development
* Strong ecosystem
* Real-time UI updates

## Event Schema Design

JSONL was selected because:

* Simple append-only structure
* Easy analytics processing
* Human readable
* Suitable for streaming events

Example Event:

{
"timestamp": "2025-06-04T10:00:00",
"event_type": "entry",
"camera": "entry_1",
"person_id": "P001"
}

## API Architecture Decisions

Store-centric architecture:

/stores/{store_id}/metrics

/stores/{store_id}/funnel

/stores/{store_id}/heatmap

/stores/{store_id}/anomalies

Benefits:

* Multi-store scalability
* Consistent endpoint structure
* Easy analytics expansion

## Analytics Design

Metrics API

Provides:

* Visitors
* Queue depth
* Conversion rate
* Abandonment rate

Heatmap API

Provides:

* Zone activity
* Dwell time
* High attention areas

Anomaly API

Provides:

* Queue spikes
* Conversion anomalies
* Operational alerts

## Production Readiness Considerations

* Modular FastAPI architecture
* Structured event logging
* Error handling
* Test folder included
* API documentation via Swagger
* Separation of frontend and backend

## Future Enhancements

* WebSocket streaming
* Customer re-identification
* Cloud-native deployment
* Distributed analytics pipeline
* Advanced anomaly detection models

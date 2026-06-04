# DESIGN DOCUMENT

## System Architecture

The system consists of three layers:

1. Video Processing Layer
2. Analytics Layer
3. API and Dashboard Layer

Video feeds are processed using OpenCV and YOLOv8. Detected events are transformed into analytics and exposed through FastAPI endpoints.

## Processing Pipeline

Video Input

↓

Person Detection

↓

Event Generation

↓

JSONL Event Logging

↓

Analytics Computation

↓

REST APIs

↓

React Dashboard

## Event Flow

Entry Camera

* Detect customer entry
* Generate entry event

Billing Camera

* Monitor queue depth
* Generate queue events

Zone Camera

* Track customer dwell time
* Generate zone visit events

## Analytics

### Funnel Analytics

Entry → Zone Visit → Billing Queue → Purchase

### Heatmap Analytics

Tracks customer attention across store zones.

### Anomaly Detection

Detects:

* Queue spikes
* Low conversion rates
* Unusual traffic patterns

## Staff Exclusion

The design supports exclusion logic by maintaining separate tracking identifiers and ignoring predefined staff regions when required.

## Edge Cases

* Re-entry detection
* Occlusions
* Partial visibility
* Camera frame drops
* Empty store scenarios

## AI-Assisted Decisions

AI tools were used to assist with:

* API design suggestions
* Dashboard structure recommendations
* Analytics pipeline refinement
* Documentation drafting
* Code debugging assistance

All implementation decisions were reviewed and validated manually before integration.

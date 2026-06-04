# AI-Powered Store Intelligence System
✅ Live Frontend Deployment
https://ai-powered-store-intelligence-syste-tau.vercel.app

## Overview

AI-Powered Store Intelligence System is a retail analytics platform that processes CCTV footage and generates real-time operational insights. The system detects customer movement, queue formation, zone activity, and store performance metrics while exposing analytics through REST APIs and a React dashboard.

## Features

* Customer Entry Detection
* Queue Monitoring
* Zone Intelligence
* Heatmap Analytics
* Funnel Analytics
* Anomaly Detection
* Live CCTV Event Tracking
* Real-Time Dashboard
* REST API Endpoints
* JSONL Event Logging

## Architecture

Frontend:

* React
* Vite

Backend:

* FastAPI
* OpenCV
* YOLOv8

Analytics:

* Funnel Analysis
* Heatmap Generation
* Queue Analytics
* Event Intelligence

## API Endpoints

GET /stores/store_1076/metrics

GET /stores/store_1076/funnel

GET /stores/store_1076/heatmap

GET /stores/store_1076/anomalies

GET /live-tracking

POST /events/ingest

## Setup

Backend

pip install -r requirements.txt

uvicorn app.main:app --reload

Frontend

cd frontend-dashboard

npm install

npm run dev

## Event Schema

Each event is stored in JSONL format.

Example:

{"timestamp":"2025-06-04T10:00:00","event_type":"entry","camera":"entry_1"}

## Testing

Run:

pytest

## Deployment

Frontend: Vercel

Backend: Render

Swagger Documentation:

/docs

## Assumptions

* CCTV feeds are pre-recorded videos.
* YOLOv8 is used for person detection.
* Store zones are predefined.
* Analytics are store-specific.

## Future Improvements

* Multi-camera tracking
* Customer re-identification
* Staff exclusion improvements
* Real-time WebSocket updates
* Cloud deployment pipeline

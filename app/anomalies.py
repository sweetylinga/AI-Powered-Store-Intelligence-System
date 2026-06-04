from fastapi import APIRouter

router = APIRouter()

@router.get("/stores/{store_id}/anomalies")
def get_anomalies(store_id: str):
    return {
        "anomalies": [
            {
                "type": "Queue Spike",
                "message": "Billing queue increased suddenly"
            },
            {
                "type": "Low Conversion",
                "message": "Visitors not converting to purchase"
            }
        ]
    }
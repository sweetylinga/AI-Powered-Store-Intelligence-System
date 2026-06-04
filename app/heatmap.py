from fastapi import APIRouter

router = APIRouter()

@router.get("/stores/{store_id}/heatmap")
def get_heatmap(store_id: str):
    return {
        "high_attention_zone": "Electronics",
        "dwell_time": 40,
        "zones": [
            {
                "zone": "Electronics",
                "visitors": 8,
                "attention": "HIGH"
            },
            {
                "zone": "Billing",
                "visitors": 3,
                "attention": "MEDIUM"
            },
            {
                "zone": "Entrance",
                "visitors": 5,
                "attention": "LOW"
            }
        ]
    }
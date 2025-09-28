from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

shipments = [
    {"tracking_id": 1, "content": "wooden table", "status": "in transit"},
    {"tracking_id": 2, "content": "metal chair", "status": "delivered"},
    {"tracking_id": 3, "content": "plastic cup", "status": "pending"},
    {"tracking_id": 4, "content": "glass bottle", "status": "in transit"},
    {"tracking_id": 5, "content": "ceramic plate", "status": "delivered"},
    {"tracking_id": 6, "content": "cotton shirt", "status": "pending"},
]


@app.get("/latest-shipment")
def get_latest_shipment():
    return max(shipments, key=lambda x: x["tracking_id"])


@app.get("/shipment/{tracking_id}")
def get_shipment(tracking_id: int):
    try:
        return next(s for s in shipments if s["tracking_id"] == tracking_id)
    except StopIteration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with tracking_id {tracking_id} not found",
        )


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url, title="Scalar API Reference"
    )


@app.post("/shipment")
def submit_shipment(content: dict) -> dict[str, str | int]:
    new_shipment = {
        "tracking_id": len(shipments) + 1,
        "content": content.get("content", "unknown"),
        "status": content.get("status", "pending"),
    }
    shipments.append(new_shipment)
    return new_shipment

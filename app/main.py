from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from .schemas import Shipment, ShipmentUpdate, ShipmentStatus, ShipmentResponse

app = FastAPI()


shipments: list[Shipment] = [
    Shipment(tracking_id=1, content="wooden table", status=ShipmentStatus.IN_TRANSIT),
    Shipment(tracking_id=2, content="metal chair", status=ShipmentStatus.DELIVERED),
    Shipment(tracking_id=3, content="plastic cup", status=ShipmentStatus.PLACED),
    Shipment(tracking_id=4, content="glass bottle", status=ShipmentStatus.IN_TRANSIT),
    Shipment(tracking_id=5, content="ceramic plate", status=ShipmentStatus.DELIVERED),
    Shipment(tracking_id=6, content="cotton shirt", status=ShipmentStatus.PLACED),
]


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url, title="Scalar API Reference"
    )


@app.get("/shipment")
def get_shipments() -> list[Shipment]:
    return shipments


@app.get("/latest-shipment")
def get_latest_shipment() -> ShipmentResponse:
    latest_shipment = max(shipments, key=lambda x: x.tracking_id)
    return ShipmentResponse(
        content=latest_shipment.content, status=latest_shipment.status
    )


@app.get("/shipment/{tracking_id}")
def get_shipment(tracking_id: int) -> ShipmentResponse:
    shipment = next((s for s in shipments if s.tracking_id == tracking_id), None)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with tracking_id {tracking_id} not found",
        )
    return shipment


@app.post("/shipment")
def submit_shipment(shipment: Shipment) -> ShipmentResponse:
    new_shipment = Shipment(
        tracking_id=len(shipments) + 1,
        content=shipment.content,
        status=shipment.status,
    )
    shipments.append(new_shipment)
    return new_shipment


@app.put("/shipment/{tracking_id}")
def update_shipment(tracking_id: int, shipment: Shipment) -> ShipmentResponse:
    shipment = get_shipment(tracking_id)
    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with tracking_id {tracking_id} not found",
        )
    shipment.content = shipment.content
    shipment.status = shipment.status
    return shipment


@app.patch("/shipment/{tracking_id}")
def shipment_update_partial(tracking_id: int, shipment: ShipmentUpdate) -> ShipmentResponse:
    shipment_update = get_shipment(tracking_id)
    if not shipment_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with tracking_id {tracking_id} not found",
        )
    if shipment.content is not None:
        shipment_update.content = shipment.content
    if shipment.status is not None:
        shipment_update.status = shipment.status
    return shipment_update


@app.delete("/shipment/{tracking_id}")
def delete_shipment(tracking_id: int):
    shipment = get_shipment(tracking_id)
    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with tracking_id {tracking_id} not found",
        )
    shipments.remove(shipment)
    return {"detail": f"Shipment with tracking_id {tracking_id} deleted"}

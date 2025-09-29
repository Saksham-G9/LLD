from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from .schemas import Shipment, ShipmentUpdate, ShipmentResponse
from .database import Database

app = FastAPI()

database = Database()


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url, title="Scalar API Reference"
    )


@app.get("/shipment")
def get_shipments() -> list[Shipment]:
    return database.get_all()


@app.get("/latest-shipment")
def get_latest_shipment() -> ShipmentResponse:
    shipments = database.get_all()
    if not shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No shipments found",
        )
    latest_shipment = max(shipments, key=lambda x: x.tracking_id)
    return ShipmentResponse(
        content=latest_shipment.content, status=latest_shipment.status
    )


@app.get("/shipment/{tracking_id}")
def get_shipment(tracking_id: int) -> ShipmentResponse:
    shipment = database.get(tracking_id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with tracking_id {tracking_id} not found",
        )
    return ShipmentResponse(content=shipment.content, status=shipment.status)


@app.post("/shipment")
def submit_shipment(shipment: Shipment) -> Shipment:
    new_tracking_id = database.create(shipment)
    new_shipment = Shipment(
        tracking_id=new_tracking_id,
        content=shipment.content,
        status=shipment.status,
    )
    return new_shipment


@app.put("/shipment/{tracking_id}")
def update_shipment(tracking_id: int, shipment: Shipment) -> Shipment:
    existing = database.get(tracking_id)
    if existing is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with tracking_id {tracking_id} not found",
        )
    updated = database.update(tracking_id, ShipmentUpdate(content=shipment.content, status=shipment.status))
    return updated


@app.patch("/shipment/{tracking_id}")
def shipment_update_partial(
    tracking_id: int, shipment: ShipmentUpdate
) -> Shipment:
    existing = database.get(tracking_id)
    if existing is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with tracking_id {tracking_id} not found",
        )
    updated = database.update(tracking_id, shipment)
    return updated


@app.delete("/shipment/{tracking_id}")
def delete_shipment(tracking_id: int):
    deleted = database.delete(tracking_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with tracking_id {tracking_id} not found",
        )
    return {"detail": f"Shipment with tracking_id {tracking_id} deleted"}

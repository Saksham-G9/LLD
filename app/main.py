from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from pydantic import BaseModel

app = FastAPI()


class Shipment(BaseModel):
    tracking_id: int
    content: str
    status: str


class ShipmentUpdate(BaseModel):
    content: str | None = None
    status: str | None = None


shipments: list[Shipment] = [
    Shipment(tracking_id=1, content="wooden table", status="in transit"),
    Shipment(tracking_id=2, content="metal chair", status="delivered"),
    Shipment(tracking_id=3, content="plastic cup", status="pending"),
    Shipment(tracking_id=4, content="glass bottle", status="in transit"),
    Shipment(tracking_id=5, content="ceramic plate", status="delivered"),
    Shipment(tracking_id=6, content="cotton shirt", status="pending"),
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
def get_latest_shipment() -> Shipment:
    return max(shipments, key=lambda x: x.tracking_id)


@app.get("/shipment/{tracking_id}")
def get_shipment(tracking_id: int) -> Shipment:
    shipment = next((s for s in shipments if s.tracking_id == tracking_id), None)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with tracking_id {tracking_id} not found",
        )
    return shipment


@app.post("/shipment")
def submit_shipment(shipment: Shipment) -> Shipment:
    new_shipment = Shipment(
        tracking_id=len(shipments) + 1,
        content=shipment.content,
        status=shipment.status,
    )
    shipments.append(new_shipment)
    return new_shipment


@app.put("/shipment/{tracking_id}")
def shipment_update(tracking_id: int, shipment: Shipment) -> Shipment:
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
def shipment_update_partial(tracking_id: int, shipment: ShipmentUpdate) -> Shipment:
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

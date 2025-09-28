from enum import Enum
from pydantic import BaseModel, Field


class ShipmentStatus(str, Enum):
    PLACED = "placed"
    IN_TRANSIT = "in transit"
    OUT_FOR_DELIVERY = "out for delivery"
    DELIVERED = "delivered"


class Shipment(BaseModel):
    tracking_id: int
    content: str = Field(max_length=30, examples=["Books"])
    status: ShipmentStatus = Field(examples=["in transit"])

class ShipmentResponse(BaseModel):
    content: str
    status: ShipmentStatus

class ShipmentUpdate(BaseModel):
    content: str | None = Field(
        default=None,
        max_length=30,
        examples=["Books"],
    )
    status: ShipmentStatus | None = Field(
        default=None,
        examples=["in transit"],
    )

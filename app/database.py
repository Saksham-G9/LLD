import json
import os

from app.schemas import Shipment, ShipmentStatus

shipments = []

path = os.path.join(os.path.dirname(__file__), "shipments.json")
with open(path, "r") as file:
    shipments_list = json.load(file)

    for shipment in shipments_list:
        try:
            new_shipment = Shipment(
                tracking_id=shipment["tracking_id"],
                content=shipment["content"],
                status=ShipmentStatus(shipment["status"]),
            )
        except Exception as e:
            print(f"Error loading shipment {shipment}: {e}")
            continue
        shipments.append(new_shipment)


def convert_shipment_to_dict(shipment: Shipment) -> dict:
    return {
        "tracking_id": shipment.tracking_id,
        "content": shipment.content,
        "status": shipment.status.value,
    }


def update_json_file(shipments) -> None:
    path = os.path.join(os.path.dirname(__file__), "shipments.json")
    shipments_dict = [
        convert_shipment_to_dict(shipment) for shipment in shipments
    ]
    with open(path, "w") as file:
        json.dump(shipments_dict, file, default=str)

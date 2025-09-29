import sqlite3

from app.schemas import Shipment, ShipmentUpdate


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("shipments.db")

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS shipments (
            tracking_id INTEGER PRIMARY KEY,
            content TEXT NOT NULL,
            status TEXT NOT NULL
            )
        """
        )

    def get_all(self) -> list[Shipment]:
        self.cursor.execute("SELECT tracking_id, content, status FROM shipments")
        results = self.cursor.fetchall()
        return [Shipment(tracking_id=r[0], content=r[1], status=r[2]) for r in results]

    def create(self, shipment: Shipment) -> int:
        self.cursor.execute(
            "INSERT INTO shipments (content, status) VALUES (?, ?)",
            (shipment.content, shipment.status),
        )
        self.commit()
        return self.cursor.lastrowid

    def get(self, tracking_id: int) -> Shipment | None:
        self.cursor.execute(
            "SELECT tracking_id, content, status FROM shipments WHERE tracking_id = ?", (tracking_id,)
        )
        result = self.cursor.fetchone()
        if result:
            return Shipment(tracking_id=result[0], content=result[1], status=result[2])
        return None

    def update(self, tracking_id: int, shipment_update: ShipmentUpdate) -> Shipment | None:
        update_fields = []
        params = {"tracking_id": tracking_id}
        if shipment_update.content is not None:
            update_fields.append("content = :content")
            params["content"] = shipment_update.content
        if shipment_update.status is not None:
            update_fields.append("status = :status")
            params["status"] = shipment_update.status
        if update_fields:
            query = f"UPDATE shipments SET {', '.join(update_fields)} WHERE tracking_id = :tracking_id"
            self.cursor.execute(query, params)
            self.commit()
        return self.get(tracking_id)

    def delete(self, tracking_id: int) -> bool:
        self.cursor.execute(
            "DELETE FROM shipments WHERE tracking_id = ?", (tracking_id,)
        )
        self.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

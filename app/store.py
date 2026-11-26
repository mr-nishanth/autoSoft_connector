"""In-memory order tracking store with two sample orders."""

from __future__ import annotations

from typing import Optional, TypedDict


class OrderRecord(TypedDict):
    order_id: str
    status: str
    updated_at: str


ORDERS: dict[str, OrderRecord] = {
    "ORD-1001": {
        "order_id": "ORD-1001",
        "status": "shipped",
        "updated_at": "2024-05-01T10:00:00+00:00",
    },
    "ORD-1002": {
        "order_id": "ORD-1002",
        "status": "pending",
        "updated_at": "2024-05-02T12:30:00+00:00",
    },
}


def get_order(order_id: str) -> Optional[OrderRecord]:
    """Return the tracking record for ``order_id`` or ``None`` if unknown."""
    record = ORDERS.get(order_id)
    return dict(record) if record is not None else None  # type: ignore[return-value]

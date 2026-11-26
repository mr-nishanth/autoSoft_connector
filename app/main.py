"""FastAPI application exposing order tracking."""

from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.store import get_order

app = FastAPI(title="AutoSoft Connector API")


class OrderTrackingResponse(BaseModel):
    order_id: str
    status: Literal["pending", "shipped", "delivered"]
    updated_at: str  # ISO 8601, UTC


@app.get(
    "/api/v1/orders/{order_id}/tracking",
    response_model=OrderTrackingResponse,
    responses={404: {"description": "Unknown order id"}},
)
def get_order_tracking(order_id: str) -> OrderTrackingResponse:
    record = get_order(order_id)
    if record is None:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return OrderTrackingResponse(**record)

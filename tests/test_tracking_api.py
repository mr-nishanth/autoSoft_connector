from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.store import ORDERS

client = TestClient(app)

ALLOWED_STATUSES = {"pending", "shipped", "delivered"}
CONTRACT_FIELDS = {"order_id", "status", "updated_at"}


def _url(order_id: str) -> str:
    return f"/api/v1/orders/{order_id}/tracking"


@pytest.mark.parametrize("order_id", ["ORD-1001", "ORD-1002"])
def test_known_order_returns_tracking(order_id):
    response = client.get(_url(order_id))
    assert response.status_code == 200
    body = response.json()
    assert body["order_id"] == order_id
    assert body["status"] == ORDERS[order_id]["status"]
    assert body["updated_at"] == ORDERS[order_id]["updated_at"]


def test_store_has_exactly_two_sample_orders():
    assert set(ORDERS) == {"ORD-1001", "ORD-1002"}


def test_response_has_exact_contract_fields():
    response = client.get(_url("ORD-1001"))
    assert set(response.json().keys()) == CONTRACT_FIELDS


@pytest.mark.parametrize("order_id", ["ORD-1001", "ORD-1002"])
def test_status_is_allowed_value(order_id):
    assert client.get(_url(order_id)).json()["status"] in ALLOWED_STATUSES


@pytest.mark.parametrize("order_id", ["ORD-1001", "ORD-1002"])
def test_updated_at_is_iso8601(order_id):
    value = client.get(_url(order_id)).json()["updated_at"]
    assert isinstance(value, str)
    parsed = datetime.fromisoformat(value)
    assert parsed.tzinfo is not None


def test_unknown_order_returns_404():
    response = client.get(_url("ORD-9999"))
    assert response.status_code == 404
    assert isinstance(response.json().get("detail"), str)

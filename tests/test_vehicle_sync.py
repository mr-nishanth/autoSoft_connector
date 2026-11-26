"""Offline tests for sync_vehicle using a fake client (no network)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List

import pytest

from autosoft_connector import VehicleInputError, sync_vehicle


# Stand-ins mirroring automate_connector's error hierarchy (not imported).
class ReynoldsError(Exception):
    pass


class VehicleNotFoundError(ReynoldsError):
    pass


class ReynoldsServerError(ReynoldsError):
    pass


class ReynoldsTransportError(ReynoldsError):
    pass


class InvalidResponseError(ReynoldsError):
    pass


@dataclass
class FakeVehicleRecord:
    vin: str
    make: str
    model: str
    year: int


class FakeClient:
    """Implements the get_vehicle(vin) interface of the automate client."""

    def __init__(self, result: Any = None, error: BaseException | None = None):
        self.result = result
        self.error = error
        self.calls: List[str] = []

    def get_vehicle(self, vin: str) -> Any:
        self.calls.append(vin)
        if self.error is not None:
            raise self.error
        return self.result


VALID_VIN = "1HGCM82633A004352"


def test_maps_vehicle_record_to_autosoft_format():
    record = FakeVehicleRecord(vin=VALID_VIN, make="Honda", model="Accord", year=2003)
    client = FakeClient(result=record)

    result = sync_vehicle(VALID_VIN, client)

    assert result == {
        "vehicle_id": VALID_VIN,
        "manufacturer": "Honda",
        "model_name": "Accord",
        "model_year": 2003,
    }
    assert set(result) == {"vehicle_id", "manufacturer", "model_name", "model_year"}


def test_calls_client_get_vehicle_once_with_vin():
    client = FakeClient(result=FakeVehicleRecord(VALID_VIN, "Honda", "Accord", 2003))

    sync_vehicle(VALID_VIN, client)

    assert client.calls == [VALID_VIN]


@pytest.mark.parametrize(
    "bad_vin",
    [
        "",
        "1HGCM82633A00435",  # 16 chars
        "1HGCM82633A0043521",  # 18 chars
        "1HGCM82633A00435I",  # contains I
        "1HGCM82633A00435O",  # contains O
        "1HGCM82633A00435Q",  # contains Q
        "1hgcm82633a004352",  # lowercase
        "1HGCM82633A00435-",  # punctuation
        None,
        12345,
        b"1HGCM82633A004352",
    ],
)
def test_invalid_vin_rejected_before_client_call(bad_vin):
    client = FakeClient(result=FakeVehicleRecord(VALID_VIN, "Honda", "Accord", 2003))

    with pytest.raises(VehicleInputError):
        sync_vehicle(bad_vin, client)

    assert client.calls == []


@pytest.mark.parametrize(
    "error",
    [
        VehicleNotFoundError("not found"),
        ReynoldsError("unprocessable"),
        ReynoldsServerError("server"),
        ReynoldsTransportError("transport"),
        InvalidResponseError("bad body"),
    ],
)
def test_client_errors_propagate(error):
    client = FakeClient(error=error)

    with pytest.raises(type(error)) as excinfo:
        sync_vehicle(VALID_VIN, client)

    assert excinfo.value is error
    assert client.calls == [VALID_VIN]

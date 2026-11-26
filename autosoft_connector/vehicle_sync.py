"""Sync a vehicle from the Automate/Reynolds client into the Autosoft format.

The upstream client (automate_connector) exposes ``get_vehicle(vin)`` returning a
``VehicleRecord`` with the attributes ``vin``, ``make``, ``model`` and ``year``.
This module depends only on that attribute shape; it does not import the
upstream package. Client errors are propagated unchanged.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Protocol

__all__ = ["VehicleClient", "VehicleInputError", "sync_vehicle"]

_VIN_LENGTH = 17
# Uppercase A-Z/0-9 excluding I, O and Q (backend VIN rule).
_VIN_PATTERN = re.compile(r"^[A-HJ-NPR-Z0-9]{17}$")


class VehicleInputError(ValueError):
    """Raised when the VIN passed to sync_vehicle is invalid."""


class VehicleClient(Protocol):
    """Interface the worker expects from the automate_connector client."""

    def get_vehicle(self, vin: str) -> Any:  # returns a VehicleRecord-like object
        ...


def _validate_vin(vin: object) -> str:
    if not isinstance(vin, str):
        raise VehicleInputError(
            f"VIN must be a str, got {type(vin).__name__}"
        )
    if len(vin) != _VIN_LENGTH:
        raise VehicleInputError(
            f"VIN must be exactly {_VIN_LENGTH} characters, got {len(vin)}"
        )
    if not _VIN_PATTERN.fullmatch(vin):
        raise VehicleInputError(
            "VIN must contain only uppercase A-Z and 0-9 excluding I, O and Q"
        )
    return vin


def sync_vehicle(vin: str, client: VehicleClient) -> Dict[str, Any]:
    """Fetch a vehicle via ``client.get_vehicle(vin)`` and map it to Autosoft format.

    Returns a dict with keys ``vehicle_id``, ``manufacturer``, ``model_name``
    and ``model_year``. Input is validated before the client is called; any
    exception raised by the client propagates unchanged.
    """
    _validate_vin(vin)
    record = client.get_vehicle(vin)
    return {
        "vehicle_id": record.vin,
        "manufacturer": record.make,
        "model_name": record.model,
        "model_year": record.year,
    }

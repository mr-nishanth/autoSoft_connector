"""AutoSoft connector package."""

from autosoft_connector.vehicle_sync import (
    VehicleClient,
    VehicleInputError,
    sync_vehicle,
)

CONNECTOR_NAME = "autosoft"

__all__ = ["CONNECTOR_NAME", "VehicleClient", "VehicleInputError", "sync_vehicle"]

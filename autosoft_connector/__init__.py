"""AutoSoft connector package."""

VERSION = "0.1.0"

from autosoft_connector.vehicle_sync import (
    VehicleClient,
    VehicleInputError,
    sync_vehicle,
)

__all__ = ["VehicleClient", "VehicleInputError", "sync_vehicle"]

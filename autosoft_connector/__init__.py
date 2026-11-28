"""AutoSoft connector package."""

from autosoft_connector.vehicle_sync import (
    VehicleClient,
    VehicleInputError,
    normalise_vin,
    sync_vehicle,
)

__all__ = ["VehicleClient", "VehicleInputError", "normalise_vin", "sync_vehicle"]

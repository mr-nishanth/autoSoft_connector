"""Offline tests for the CONNECTOR_NAME constant (no network)."""

import autosoft_connector


def test_connector_name_value():
    assert autosoft_connector.CONNECTOR_NAME == "autosoft"


def test_connector_name_is_str():
    assert isinstance(autosoft_connector.CONNECTOR_NAME, str)


def test_connector_name_exported():
    assert "CONNECTOR_NAME" in autosoft_connector.__all__

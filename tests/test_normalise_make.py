import pytest

import autosoft_connector
from autosoft_connector import VehicleInputError, normalise_make


def test_lowercase_input_is_title_cased():
    assert normalise_make("honda") == "Honda"


def test_surrounding_and_internal_whitespace_is_stripped_and_collapsed():
    assert normalise_make("  land   rover  ") == "Land Rover"


def test_empty_string_raises():
    with pytest.raises(VehicleInputError):
        normalise_make("")


def test_whitespace_only_string_raises():
    with pytest.raises(VehicleInputError):
        normalise_make("   \t ")


@pytest.mark.parametrize("value", [None, 123, b"honda"])
def test_non_string_raises(value):
    with pytest.raises(VehicleInputError):
        normalise_make(value)


def test_normalise_make_is_exported():
    assert "normalise_make" in autosoft_connector.__all__
    assert autosoft_connector.normalise_make is normalise_make

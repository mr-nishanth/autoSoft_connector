import autosoft_connector


def test_version_is_non_empty_string():
    assert isinstance(autosoft_connector.VERSION, str)
    assert autosoft_connector.VERSION != ""


def test_version_has_three_numeric_parts():
    parts = autosoft_connector.VERSION.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)

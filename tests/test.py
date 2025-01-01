import pytest
from easy_adb_controller import AndroidDevice


def test_initialization_valid():
    """Test if initialization works correctly with valid inputs."""
    adb_device = AndroidDevice(ip="127.0.0.1", port=5037)
    assert adb_device is not None


def test_invalid_ip():
    """Test invalid IP address during initialization."""
    with pytest.raises(ValueError):
        AndroidDevice(ip="", port=5037)

    with pytest.raises(ValueError):
        AndroidDevice(ip=None, port=5037)


def no_device_found():
    with pytest.raises(ConnectionError):
        AndroidDevice(ip="127.0.0.1", port=5037)

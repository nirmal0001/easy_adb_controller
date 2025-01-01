import sys

import pytest

sys.path.append("/home/nimma/Projects/Python/easy_adb_controller")
from src.android_device import AndroidDevice


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


def test_no_device_found():
    try:
        device = AndroidDevice(ip="127.0.0.1", port=5037)
        assert device is not None
    except ConnectionError:
        assert True is True


def test_uninstall_app():
    adb_device = AndroidDevice(ip="127.0.0.1", port=5037)
    adb_device.uninstall_app("com.afwsamples.testdpc")
    assert adb_device.device.is_installed("com.afwsamples.testdpc") is False


def test_install_app():
    adb_device = AndroidDevice(ip="127.0.0.1", port=5037)
    adb_device.install_app("tests/sample.apk")
    assert adb_device.device.is_installed("com.afwsamples.testdpc") is True

from ._types import AndroidPermissions, KeyCode
from .android_device import AndroidDevice
from .logger import setup_logger

# Set up package-wide logger
logger = setup_logger(name="android_controller", log_file="android_controller.log")
__all__ = ["AndroidDevice", "AndroidPermissions", "KeyCode", "logger"]

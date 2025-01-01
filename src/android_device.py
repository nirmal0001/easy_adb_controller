"""Android controller in python using pure-python-adb."""

import logging

import requests
from ppadb.client import Client as AdbClient
from ppadb.device import Device

logger = logging.getLogger(__name__)


class AndroidDevice:
    """Control Android using adb with enhanced input validation and logging.
    ip: str: IP address of the Android device.
    port: int: Port number of the Android device.
    ocr_key: str: API key for OCR from api-ninjas.com. (Optional)
    """

    def __init__(self, ip: str, port: int, ocr_key: str = None):
        if not isinstance(ip, str) or not ip:
            raise ValueError("IP address must be a non-empty string.")
        if not isinstance(port, int) or port <= 0:
            raise ValueError("Port must be a positive integer.")

        self.client = AdbClient(host=ip, port=port)
        devices = self.client.devices()
        if not devices:
            raise ConnectionError("No devices connected or found.")
        elif len(devices) > 1:
            raise ConnectionError("More then one device found.")

        self.device: Device = devices[0]
        self.ocr_api_key = ocr_key
        logger.info("Connected to %s:%i", ip, port)

    def execute_shell_command(self, command: str):
        """Execute shell command."""
        if not isinstance(command, str) or not command:
            raise ValueError("Command must be a non-empty string.")
        self.device.shell(command)
        logger.info("Executed shell command: %s", command)

    def simulate_touch(self, x: int, y: int):
        """Simulate a tap or touch."""
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Coordinates must be integers.")
        self.execute_shell_command(f"input tap {x} {y}")
        logger.info("Simulated touch at (%s , %s)", x, y)

    def clear_input(self, length: int = 40):
        """Clear input if it's selected.
        length: int: Length of the input to clear.
        """
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Length must be a positive integer.")
        for _ in range(length):
            self.execute_shell_command("input keyevent KEYCODE_DEL")
        logger.info("Input cleared")

    def press_enter(self):
        """Press keyboard enter button."""
        self.execute_shell_command("input keyevent 66")
        logger.info("Pressed Enter")

    def press_key(self, key_code: int):
        """Press a key on the keyboard.
        keycode: int: Key code to press. (check code from .KeyCode )
        """
        if not isinstance(key_code, int) or key_code <= 0:
            raise ValueError("Key code must be a positive integer.")
        self.execute_shell_command(f"input keyevent {key_code}")
        logger.info("Pressed key with code: %s", key_code)

    def enter_text(self, text: str):
        """Enter text.
        text: str: Text to enter.
        """
        if not isinstance(text, str) or not text:
            raise ValueError("Text must be a non-empty string.")
        self.execute_shell_command(f'input text "{text}"')
        logger.info("Entered text: %s", text)

    def connect_to_proxy(self, proxy_ip: str, proxy_port: int):
        """Connect to a proxy on Android.
        proxy_ip: str: Proxy IP address.
        proxy_port: int: Proxy port.
        """
        if not isinstance(proxy_ip, str) or not proxy_ip:
            raise ValueError("Proxy IP must be a non-empty string.")
        if not isinstance(proxy_port, int) or proxy_port <= 0:
            raise ValueError("Proxy port must be a positive integer.")
        self.execute_shell_command(
            f"settings put global http_proxy {proxy_ip}:{proxy_port}"
        )
        logger.info("Connected to proxy %s:%i", proxy_ip, proxy_port)

    def disconnect_proxy(self):
        """Disconnect from proxy."""
        self.execute_shell_command("settings put global http_proxy :0")
        logger.info("Proxy disconnected")

    def open_app(self, package_name: str, activity_name: str = None):
        """Open an Android app with or without an activity.
        package_name: str: Package name of the app. (Required)
        activity_name: str: Activity name of the app. (Optional)
        """
        if not package_name or not isinstance(package_name, str):
            raise ValueError("Package name must be a non-empty string.")
        if activity_name is None:
            self.execute_shell_command(f"am start -n {package_name}")
            logger.info("Opened app: %s.", package_name)
        else:
            if not activity_name or not isinstance(activity_name, str):
                raise ValueError("Activity name must be a non-empty string.")
            self.execute_shell_command(f"am start -n {package_name}/{activity_name}")
            logger.info(
                "Opened app: %s, with activity: %s.", package_name, activity_name
            )

    def install_app(self, pakage_location: str):
        """Install a package from a given location.
        pakage_location: str: Location of the package to install.
        """
        if pakage_location is None or not isinstance(pakage_location, str):
            raise ValueError("Package location must be a non-empty string.")
        self.device.install(pakage_location)
        logger.info("Installed app from %s", pakage_location)

    def uninstall_app(self, package_name: str):
        """Uninstall an app.
        pakage_name: str: Package name of the app.
        """
        if not package_name or not isinstance(package_name, str):
            raise ValueError("Package name must be a non-empty string.")
        self.device.uninstall(package_name)
        logger.info("Uninstalled app: %s", package_name)

    def clear_app_data(self, package_name: str):
        """Clear app data."""
        if not package_name or not isinstance(package_name, str):
            raise ValueError("Package name must be a non-empty string.")
        self.execute_shell_command(f"pm clear {package_name}")
        logger.info("Cleared app data for %s", package_name)

    def grant_permissions(self, package_name: str, permissions: list):
        """Grant required permissions to an app.
        pakage_name: str: Package name of the app.
        permissions: list: List of permissions to grant.
        """
        if not package_name or not isinstance(package_name, str):
            raise ValueError("Package name must be a non-empty string.")
        if not isinstance(permissions, list) or not all(
            isinstance(p, str) for p in permissions
        ):
            raise ValueError("Permissions must be a list of non-empty strings.")
        for permission in permissions:
            self.execute_shell_command(f"pm grant {package_name} {permission}")
        logger.info("Granted permissions to %s", package_name)

    def capture_screenshot(
        self,
        local_path: str = "screenshot.png",
    ):
        """Capture a screenshot and pull it to local storage.
        local_path: str: Local path to save the screenshot.
        """
        if not isinstance(local_path, str) or not local_path:
            raise ValueError("Local path must be a non-empty string.")
        result = self.device.screencap()
        with open(local_path, "wb") as fp:
            fp.write(result)
        logger.info("Screenshot captured and saved to %s", local_path)

    def check_text_in_screenshot(
        self, text: list[str] | str, response: str = None
    ) -> bool:
        """Check if a given text is present in a screenshot using OCR.
        text: list: List of text to check in the screenshot or Single text.
        response: str: OCR response to check the text in. If None, OCR will be performed.
        """
        if response is None or self.ocr_api_key is None:
            logger.error("OCR API key is not initialized. Initialize with a valid key.")
            return False
        if not isinstance(text, list) or not isinstance(text, str):
            raise ValueError("Text must be a non-empty string or list of text.")
        if response is None:
            response = self.extract_text()
        if response in (None, False):
            return False
        else:
            response = response.lower()
            if isinstance(text, list):
                for t in text:
                    try:
                        if t.lower() in response:
                            return True
                    except Exception as e:
                        logger.error("Error in text comparison: %s", e)
                        return False
            elif isinstance(text, str):
                try:
                    if text.lower() in response:
                        return True
                except Exception as e:
                    logger.error("Error in text comparison: %s", e)
                    return False
            logger.info("Text not found in screenshoot")
            return False

    def extract_text(self) -> str | bool:
        """extract in a screenshot using OCR."""
        self.capture_screenshot()
        api_url = "https://api.api-ninjas.com/v1/imagetotext"
        try:
            with open("screenshot.png", "rb") as image_file:
                files = {"image": image_file}
                response = requests.post(
                    api_url,
                    files=files,
                    headers={"X-Api-Key": self.ocr_api_key},
                    timeout=15,
                )

            if response.status_code == 200:
                return " ".join([text["text"] for text in response.json()])
            else:
                logger.error(
                    "Error in OCR API: %s, %s", response.status_code, response.text
                )
                return False
        except Exception as e:
            logger.error("Error during OCR process: %s", e)
            return False

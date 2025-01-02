# easy-adb-controller
A Python module for controlling Android devices using ADB (Android Debug Bridge) with enhanced input validation and logging. Built on top of [pure-python-adb](https://pypi.org/project/pure-python-adb/).

## Features
- Device connection and management
- Touch simulation and input control  
- App installation and management
- Screenshot capture and OCR capabilities
- Proxy connection handling
- Comprehensive logging
- Input validation for all operations

## Installation
```bash
pip install git+https://github.com/nirmal0001/easy_adb_controller
```

## Requirements
- Python 3.8+
- pure-python-adb.
- requests (for OCR functionality)

## Quick Start
```python
from easy_adb_controller import AndroidDevice
from easy_adb_controller import AndroidPermissions
# Connect to device
device = AndroidDevice(ip="127.0.0.1", port=5037)

# Basic operations
device.simulate_touch(x=100, y=200)
device.enter_text(text="Hello World")
device.capture_screenshot(local_path="my_screenshot.png")

# App management
device.open_app(package_name="com.example.app")
# with specific activity
device.open_app(package_name="com.example.app", activity_name="main_activity") 
device.install_app("path/to/app.apk")
device.capture_screenshot(local_path="screenshot.png")
device.extract_text()
device.check_text_in_screenshot(text=["hello", "world"])
device.clear_app_data(package_name="com.example.app")
#get all permissions from easy_adb_controller.AndroidPermissions
device.grant_permissions(package_name="com.example.app", permissions=[AndroidPermissions.WRITE_EXTERNAL_STORAGE, AndroidPermissions.READ_EXTERNAL_STORAGE]) 

# connect to proxy
device.connect_to_proxy(ip: str, port: int)
device.disconnect_proxy()
```

## Core Features

### Device Control
- Touch simulation
- Text input
- Key events
- Screenshot capture

### App Management
- Install/uninstall apps
- Open apps with specific activities
- Clear app data
- Grant permissions

### OCR Capabilities
- Extract text from screenshots
- Search for specific text in screenshots
- Requires API key from api-ninjas.com

### Proxy Management
- Connect to proxy servers
- Disconnect from proxy

## API Reference

### AndroidDevice
```python
device = AndroidDevice(ip: str, port: int, ocr_key: str = None)
```

#### Parameters
- `ip`: IP address of the Android device
- `port`: Port number for ADB connection
- `ocr_key`: Optional API key for OCR functionality (get key from api-ninjas.com)

#### Methods on device
- `simulate_touch(x: int, y: int)`
- `enter_text(text: str)`
- `open_app(package_name: str, activity_name: str = None)`
- `install_app(package_location: str)`
- `capture_screenshot(local_path: str = "screenshot.png")`
- `check_text_in_screenshot(text: list[str] | str, response: str = None) -> bool`
- `clear_app_data(package_name: str)`
- `grant_permissions(package_name: str, permissions: list[str])` get permissions from easy_adb_controller.AndroidPermissions
- `connect_to_proxy(ip: str, port: int)`
- `disconnect_proxy()`

## Error Handling
The module includes comprehensive input validation and error handling:
- Type checking for all parameters
- Connection verification
- API response validation
- Detailed error logging

## License
[MIT](/LICENSE)

## Contributing
- Fork the repository
- Create a feature branch (git checkout -b feature/amazing-feature)
- Commit your changes (git commit -m 'Add amazing feature')
- Push to the branch (git push origin feature/amazing-feature)
- Open a Pull Request
from dataclasses import dataclass


@dataclass
class KeyCode:
    """Keycode For easy adb controller"""

    Home = 3
    Back = 4
    Call = 5
    EndCall = 6
    VolumeUp = 24
    VolumeDown = 25
    Power = 26
    Camera = 27
    Clear = 28
    DpadUp = 19
    DpadDown = 20
    DpadLeft = 21
    DpadRight = 22
    DpadCenter = 23
    MediaPlay = 126
    MediaPause = 127
    MediaPlayPause = 85
    MediaStop = 86
    MediaNext = 87
    MediaPrevious = 88
    MediaRewind = 89
    MediaFastForward = 90
    Enter = 66
    Del = 67
    Space = 62
    Tab = 61
    Escape = 111
    Menu = 82
    Search = 84
    Notification = 83
    Settings = 176
    Num0 = 7
    Num1 = 8
    Num2 = 9
    Num3 = 10
    Num4 = 11
    Num5 = 12
    Num6 = 13
    Num7 = 14
    Num8 = 15
    Num9 = 16
    Plus = 81
    Minus = 69
    Star = 17
    Slash = 76


@dataclass
class AndroidPermissions:
    """Android Permissions"""

    INTERNET = "android.permission.INTERNET"
    READ_CALL_LOG = "android.permission.READ_CALL_LOG"
    ACCESS_NETWORK_STATE = "android.permission.ACCESS_NETWORK_STATE"
    READ_EXTERNAL_STORAGE = "android.permission.READ_EXTERNAL_STORAGE"
    WRITE_EXTERNAL_STORAGE = "android.permission.WRITE_EXTERNAL_STORAGE"
    WAKE_LOCK = "android.permission.WAKE_LOCK"
    FOREGROUND_SERVICE = "android.permission.FOREGROUND_SERVICE"
    ACCESS_FINE_LOCATION = "android.permission.ACCESS_FINE_LOCATION"
    ACCESS_COARSE_LOCATION = "android.permission.ACCESS_COARSE_LOCATION"
    READ_CONTACTS = "android.permission.READ_CONTACTS"
    WRITE_CONTACTS = "android.permission.WRITE_CONTACTS"
    RECORD_AUDIO = "android.permission.RECORD_AUDIO"
    CALL_PHONE = "android.permission.CALL_PHONE"
    CAMERA = "android.permission.CAMERA"
    READ_MEDIA_AUDIO = "android.permission.READ_MEDIA_AUDIO"
    READ_MEDIA_IMAGES = "android.permission.READ_MEDIA_IMAGES"
    READ_MEDIA_VIDEO = "android.permission.READ_MEDIA_VIDEO"
    POST_NOTIFICATIONS = "android.permission.POST_NOTIFICATIONS"
    RECEIVE_BOOT_COMPLETED = "android.permission.RECEIVE_BOOT_COMPLETED"
    BLUETOOTH = "android.permission.BLUETOOTH"
    BLUETOOTH_ADMIN = "android.permission.BLUETOOTH_ADMIN"
    BLUETOOTH_CONNECT = "android.permission.BLUETOOTH_CONNECT"

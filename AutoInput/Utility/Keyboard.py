import time
import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)
INPUT_KEYBOARD = 1
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
MAPVK_VK_TO_VSC = 0
# msdn.microsoft.com/en-us/library/dd375731
wintypes.ULONG_PTR = wintypes.WPARAM


class MouseInput(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))


class KeyboardInput(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KeyboardInput, self).__init__(*args, **kwds)
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)


class HardwareInput(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KeyboardInput),
                    ("mi", MouseInput),
                    ("hi", HardwareInput))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))


LPINPUT = ctypes.POINTER(INPUT)


def press_key(hex_key_code):
    x = INPUT(
        type=INPUT_KEYBOARD,
        ki=KeyboardInput(wVk=hex_key_code)
    )
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def release_key(hex_key_code):
    x = INPUT(
        type=INPUT_KEYBOARD,
        ki=KeyboardInput(
            wVk=hex_key_code,
            dwFlags=KEYEVENTF_KEYUP
        )
    )
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def press_and_release_at_once(hex1, hex2, hold_time):
    press_key(hex1)
    press_key(hex2)
    time.sleep(hold_time)
    release_key(hex1)
    release_key(hex2)


def press_and_release(hex_code, hold_time):
    press_key(hex_code)
    time.sleep(hold_time)
    release_key(hex_code)


def press_and_hold(hex_code):
    press_key(hex_code)


import pyscreenshot as image_grab
import pyautogui as auto_gui
from PIL import Image, ImageOps


# This gets a screenshot of your screen
def get_screen():
    screenshot_name = "Screenie/" + "screen.png"

    image = auto_gui.grab()
    image.save(screenshot_name)

    return Image.open(screenshot_name)

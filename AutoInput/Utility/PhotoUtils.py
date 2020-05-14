import pyscreenshot as image_grab
import pyautogui as auto_gui
import AutoInput.Utility.Constants as Constants
import AutoInput.Utility.Utils as Utils
from PIL import Image, ImageOps


# This gets a screenshot of your screen
def get_screen():
    screenshot_location = Constants.MAIN_FILE_LOCATION + "/runtime/captures"
    Utils.make_directories_to_target(screenshot_location)

    screenshot_name = screenshot_location + "/screen_hour_" + str(Constants.HOURS_RUNNING) + ".png"
    Constants.HOURS_RUNNING += 1

    image = auto_gui.grab()
    image.save(screenshot_name)

    return Image.open(screenshot_name)

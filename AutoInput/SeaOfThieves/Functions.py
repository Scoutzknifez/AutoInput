import time
import AutoInput.Utility.Constants as Constants
import AutoInput.Utility.Keyboard as Keyboard
import AutoInput.Utility.PhotoUtils as PhotoUtils


def not_afk():
    PhotoUtils.get_screen()
    time.sleep(3)

    time_passed = 0
    sleep_time = 30

    while True:
        Keyboard.press_and_release(Constants.HEX_DICTIONARY['space'], .01)
        time.sleep(sleep_time)

        time_passed += sleep_time
        if time_passed >= Constants.SECONDS_IN_HOUR / 6:
            time_passed = 0
            PhotoUtils.get_screen()

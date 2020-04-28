import time
import AutoInput.Utility.Constants as Constants
import AutoInput.Utility.Utils as Utils


def start():
    if __name__ != '__main__':
        return

    time.sleep(3)

    while True:
        Utils.press_and_release(Constants.HEX_DICTIONARY['space'], .05)
        time.sleep(30)


start()

import time
import AutoInput.Utility.Constants as Constants
import AutoInput.Utility.Utils as Utils


def start():
    if __name__ != '__main__':
        return

    time.sleep(3)
    loop_sleep_time = 30

    # Conversion
    converting = True
    seconds_before_convert = 3600 / 3
    convert_loop_allowance = seconds_before_convert / loop_sleep_time

    loop_count = 0

    while True:
        Utils.press_and_release(Constants.HEX_DICTIONARY['space'], .05)
        loop_count += 1

        if converting and loop_count > convert_loop_allowance:
            Utils.press_and_release(Constants.HEX_DICTIONARY['2'], .01)
            loop_count = 0

        time.sleep(loop_sleep_time)


start()

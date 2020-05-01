import time
import AutoInput.Utility.Constants as Constants
import AutoInput.Utility.Utils as Utils

# 1 - Sprinkler
# 2 - Instant Converter
# 3 - Field Dice
# 4 - Cloud Vial
# 5 - Marshmellow Bee (30m Duration)
# 6 - Jellybean

# Not AFK settings
loop_sleep_time = 60
loop_count = 0

# Conversion Statics
converting = True
seconds_before_convert = 3600
convert_loop_allowance = seconds_before_convert / loop_sleep_time


def not_afk():
    time.sleep(3)

    while True:
        Utils.press_and_release(Constants.HEX_DICTIONARY['space'], .05)
        loop_count += 1
        do_conversion()
        time.sleep(loop_sleep_time)


def do_conversion():
    if converting and loop_count > convert_loop_allowance:
        Utils.press_and_release(Constants.HEX_DICTIONARY['2'], .01)
        loop_count = 0

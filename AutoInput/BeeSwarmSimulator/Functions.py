import time
import AutoInput.BeeSwarmSimulator.Constants as BssConstants
import AutoInput.Utility.Constants as Constants
import AutoInput.Utility.Utils as Utils

# 1 - Sprinkler
# 2 - Instant Converter
# 3 - Field Dice
# 4 - Cloud Vial
# 5 - Marshmallow Bee (30m Duration)
# 6 - Jellybean


def not_afk():
    time.sleep(3)

    while True:
        Utils.press_and_release(Constants.HEX_DICTIONARY['space'], .05)
        BssConstants.loop_count += 1
        do_conversion()
        time.sleep(BssConstants.loop_sleep_time)


def do_conversion():
    if BssConstants.converting and BssConstants.loop_count > BssConstants.convert_loop_allowance:
        Utils.press_and_release(Constants.HEX_DICTIONARY['2'], .01)
        BssConstants.loop_count = 0

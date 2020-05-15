import time
import AutoInput.BeeSwarmSimulator.Config as BssConstants
import AutoInput.Utility.Constants as Constants
import AutoInput.Utility.Keyboard as Keyboard
import AutoInput.Utility.PhotoUtils as PhotoUtils

# 1 - Sprinkler
# 2 - Instant Converter
# 3 - Field Dice
# 4 - Cloud Vial
# 5 - Marshmallow Bee (30m Cooldown)
# 6 - Jellybean (40s Cooldown)


def not_afk():
    time.sleep(3)

    while True:
        Keyboard.press_and_release(Constants.HEX_DICTIONARY[BssConstants.NOT_AFK_KEY], .01)
        BssConstants.loop_count += 1
        do_conversion()
        time.sleep(BssConstants.loop_sleep_time)


def do_conversion():
    if BssConstants.converting and BssConstants.loop_count > BssConstants.convert_loop_allowance:
        PhotoUtils.get_screen()
        # Keyboard.press_and_release(Constants.HEX_DICTIONARY[BssConstants.CONVERSION_KEY], .01)
        # BssConstants.loop_count = 0


def do_marshmallow():
    Keyboard.press_and_release(Constants.HEX_DICTIONARY[BssConstants.MARSHMALLOW_BEE_KEY], .01)

import AutoInput.Utility.Constants as Constants

# Not AFK settings
NOT_AFK_KEY = Constants.HEX_DICTIONARY['space']
loop_sleep_time = 60
loop_count = 0

# Conversion Statics
CONVERSION_KEY = Constants.HEX_DICTIONARY['2']
converting = True
seconds_before_convert = 3600
convert_loop_allowance = seconds_before_convert / loop_sleep_time

# Marshmallow Bee Settings
MARSHMALLOW_BEE_KEY = Constants.HEX_DICTIONARY['5']
MARSHMALLOW_BEE_COOLDOWN = 1800  # Seconds (Half an hour)

import AutoInput.BeeSwarmSimulator.Functions as Bss
import AutoInput.SeaOfThieves.Functions as Sot
import AutoInput.Utility.Constants as Constants
import AutoInput.Terraria.Functions as Ter
import os


def start():
    if __name__ != '__main__':
        return

    Constants.MAIN_FILE_LOCATION = os.path.dirname(__file__)

    # Bss.not_afk()
    # Sot.not_afk()
    Ter.not_afk()


start()

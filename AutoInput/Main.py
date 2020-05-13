import AutoInput.BeeSwarmSimulator.Functions as Bss
import AutoInput.Utility.Constants as Constants
import AutoInput.Utility.PhotoUtils as PU
import os


def start():
    if __name__ != '__main__':
        return

    Constants.MAIN_FILE_LOCATION = os.path.dirname(__file__)
    PU.get_screen()

    Bss.not_afk()


start()

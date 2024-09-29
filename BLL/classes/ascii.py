import GlobalVariables as Global
import os


class Ascii:
    @staticmethod
    def verify_width():
        if Global.width <= 0:
            try:
                return os.get_terminal_size().columns
            except OSError:
                return 220
        elif Global.width > 0:
            return Global.width
        else:
            return 220

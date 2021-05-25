import re

from craftbot import report


class Macro:
    """
    generate a macro object used in `Craftbot.forge()`. Time will be calculated automatically.
    - `macro`: macro content text.
    - `key`: macro shortcut key.
    """

    def __init__(self, macro, key):
        self.macro = macro
        self.key = key
        self.time = Macro.get_marco_time(self.macro)

    @staticmethod
    def get_marco_time(macro):
        # find all nums and sum.
        # return seconds.
        pattern = "[1-9]"
        result = re.findall(pattern, macro, flags=0)
        t = sum([int(x) for x in result])
        report("Macro length:", t, "sec")
        return t

    def __repr__(self):
        return self.macro+"\nkey:"+self.key+"\ntime:"+str(self.time)
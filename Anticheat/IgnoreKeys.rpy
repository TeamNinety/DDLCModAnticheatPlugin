init -998 python in AntiCheat:
    class IgnoreKeys(BaseAntiCheatModule):
        def __init__(self):
            super(IgnoreKeys, self).__init__("IgnoreKeys")


        def run(self):
            global IgnoreKeyMaps, config

            for keyName in IgnoreKeyMaps.keys():
                if IgnoreKeyMaps[keyName] is True:
                    config.keymap[keyName] = []

        def check(self):
            global IgnoreKeyMaps, config

            r = []

            for keyName in IgnoreKeyMaps.keys():
                if IgnoreKeyMaps[keyName] is True:
                    r.append(config.keymap[keyName] == [])

            return all(r)
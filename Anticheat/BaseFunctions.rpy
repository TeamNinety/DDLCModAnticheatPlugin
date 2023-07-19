
# For setting chatacters display args
init -999 python in AntiCheat:
    def setDisplayArgs(character, func):
        character.display_args["callback"] = func
        character.what_args["slow_abortable"] = config.developer

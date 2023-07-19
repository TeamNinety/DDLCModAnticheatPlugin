# Basic configuration
init -999 python in AntiCheat:
    from store import config

    ########################################################################
    # These variables are used to configure checks for value changes
    # This variable is used to control whether to log value changes
    # !! Value Checker will not check value starting with '_'
    EnableCheckingValueChanged = True

    # You can add the important variables to LogValueList
    # Or you can set it to empty list then it will log all variables in store namespace
    LogValueList = []

    # Set what variables you don't want to log
    BlockList = ()

    # After how many conversations have passed, log the value
    LogValuesAfterEveryConversations = 2
    ########################################################################


    ########################################################################
    # These variables are used to configure loggers
    # This variable is used to control whether to log AntiCheat module messages
    EnableLogger = True

    # This variable is used to record the log location
    logDir = config.basedir + "/logs"

    # This variable is used to control whether to use loguru module
    EnableLoguru = True
    ########################################################################


    ########################################################################
    # This variable is used to configure ignore key events
    # This variable is used to control whether to ignore key events
    EnableIgnoreDevelopeKeys = True

    # This variable is used to record the key maps 
    IgnoreKeyMaps = {
        "rollback": True,
        'reload_game': True,
        'launch_editor': True,
        'inspector': True,
        'full_inspector': True,
        'developer': True,
        'choose_renderer': True,
        'progress_screen': True,
        'console': False,
        'console_newer': True,
        'console_older': True,
        'director': True,
        'performance': True,
        'image_load_log': True,
        'profile_once': True,
        'memory_profile': True
    }
    ########################################################################

init -999 python in AntiCheat:
    # Write your method of judging cheating here.
    # Use the 'isCheated' function by default

    def methodOfJudgingCheating(event, interact=True, **kwargs):
        if EnableCheckingValueChanged:
            ValueChecker.run()

        # Your code
        # ...

# !! DO NOT EDIT THESE CODES !!
init -997 python in AntiCheat:
    import store

    if EnableCheckingValueChanged:
        ValueChecker = ValueChecker()
        ValueChecker.run()

    if EnableIgnoreDevelopeKeys:
        IgnoreKeys = IgnoreKeys()
        IgnoreKeys.run()

    # Set AntiCheat Namespaces to constant
    store.AntiCheat.__setattr__ = (lambda *args, **kwds: None)
    _constant = True

init python in AntiCheat:
    # Set Display Args
    setDisplayArgs(store.s, methodOfJudgingCheating)
    setDisplayArgs(store.y, methodOfJudgingCheating)
    setDisplayArgs(store.m, methodOfJudgingCheating)
    setDisplayArgs(store.n, methodOfJudgingCheating)
    setDisplayArgs(store.mc, methodOfJudgingCheating)
    setDisplayArgs(store.narrator, methodOfJudgingCheating)


# This file is used to log the AntiCheat Module Infos

# For AntiCheat Debug
init -998 python in AntiCheat:
    if EnableLogger:
        # To get system information
        import platform, os, time

        # Create the logDir if it doesn't exist.
        if not os.access(logDir, os.F_OK):
            os.mkdir(logDir)

        # Use loguru module or logging module to log messages
        if EnableLoguru == True:
            # !! DO NOT EDIT THESE CODES !!
            from loguru import _Core, _Logger
            import atexit as _atexit
            def createLogger(*args, **kwargs):
                logger = _Logger(
                    core=_Core(),
                    exception=None,
                    depth=0,
                    record=False,
                    lazy=False,
                    colors=False,
                    raw=False,
                    capture=True,
                    patchers=[],
                    extra={},
                )
                logger.add(*args, **kwargs, encoding="utf-8")
                _atexit.register(logger.remove)
                return logger

        else:
            # !! DO NOT EDIT THESE CODES !!
            import logging
            def createLogger(filename, loggerName):
                logFile = filename
                handler = logging.FileHandler(logFile)
                handler.setLevel('DEBUG')

                # 2023-06-15 20:00:54.803 | DEBUG    | __main__:<module>:1 - 1
                fmt = '%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)s - %(message)s'
                formatter = logging.Formatter(fmt)
                handler.setFormatter(formatter)

                logger = logging.getLogger(loggerName)
                logger.setLevel('DEBUG')

                logger.addHandler(handler)
                return logger

        # Format time
        t = time.strftime("%Y-%m-%d-%H_%M_%S")


        if EnableLoguru:
            # !! DO NOT EDIT THESE CODES !!
            AntiCheatLogger = createLogger(
                sink=logDir + "/AntiCheat_Log_" + t + ".log",
                level=10,
                backtrace=True,
                diagnose=True,
                catch=True,
                mode="w"
            )

        else:
            # !! DO NOT EDIT THESE CODES !!
            AntiCheatLogger = createLogger(logDir + "/AntiCheat_Log_" + t + ".log", "AntiCheatLog")

        # Get systen informations
        unameObj = platform.uname()

        # Output initialization message
        AntiCheatLogger.debug("\nAntiCheat Module Started. Runtime: " + t + " System: " + unameObj[0] + unameObj[3])

        # Delete useless variables
        del unameObj, t, logDir

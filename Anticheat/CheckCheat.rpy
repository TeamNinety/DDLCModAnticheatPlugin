init -998 python in AntiCheat:
    ## config.python_callbacks
    ## config.start_callbacks 
    ## config.quit_callbacks

    def isCheated():
        r = []
        if EnableIgnoreDevelopeKeys:
            r.append(IgnoreKeys.check())
        
        if EnableCheckingValueChanged:
            r.append(ValueChecker.check())
        
        return not all(r)

init -998 python in AntiCheat:
    class ValueChecker(BaseAntiCheatModule):

        class ValueLogger(object):
            def __init__(self, log=None):
                # {"value": {1: ..., 2: ..., 3: ...}}
                self._log = log if log else {}
                self.block_list = ('m_name', 's_name', 'y_name', 'n_name')

            def log(self, valueName, value):
                if not (valueName.startswith('_') or valueName in self.block_list or valueName in BlockList):
                    if valueName in self._log.keys():
                        d = self._log.get(valueName)
                        n = list(d.keys())[-1] + 1
                        d[n] = value
                    else:
                        self._log[valueName] = {}
                        self._log[valueName][1] = value

            def check(self, valueName, value):
                if not (valueName.startswith('_') or valueName in self.block_list or valueName in BlockList):
                    d = self._log.get(valueName)
                    n = list(d.keys())[-1]
                    return d[n] == value
                else:
                    return True

            def getValue(self, valueName):
                d = self._log.get(valueName)
                n = list(d.keys())[-1]
                return d[n]

            def __eq__(self, other):
                if not isinstance(other, self.__class__):
                    return False
                return self._log == other._log

            def __reduce__(self):
                return (self.__class__, (self._log,))


        def __init__(self, logger = None, settings = None):
            super(ValueChecker, self).__init__('ValueChecker')
            self.valueLogger = logger if logger else self.ValueLogger()
            self.count = 0

        def run(self):
            global LogValuesAfterEveryConversations, LogValueList, store
            if self.count != LogValuesAfterEveryConversations:
                self.count += 1
                return
            if not LogValueList:
                for s in vars(store):
                    value = getattr(store, s)
                    self.valueLogger.log(s, value)
            else:
                for s in LogValueList:
                    value = getattr(store, s)
                    self.valueLogger.log(s, value)
            self.count = 0

        def check(self):
            global store, LogValueList
            r = []
            # r2 = []
            if not LogValueList:
                for s in self.valueLogger._log.keys():
                    value = getattr(store, s)
                    # if self.valueLogger.check(s, value) is False:
                    #     r.append(self.valueLogger.check(s, value))
                    #     r2.append({'value': s, 'now': value, 'before': self.valueLogger.getValue(s)})
                    # else:
                    #     r.append(self.valueLogger.check(s, value))
                    r.append(self.valueLogger.check(s, value))
            else:
                for s in LogValueList:
                    value = getattr(store, s)
                    # if self.valueLogger.check(s, value) is False:
                    #     r.append(self.valueLogger.check(s, value))
                    #     r2.append({'value': s, 'now': value, 'before': self.valueLogger.getValue(s)})
                    # else:
                    #     r.append(self.valueLogger.check(s, value))
                    r.append(self.valueLogger.check(s, value))
            
            return all(r)
            # return all(r), r2

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                return False
            return self.valueLogger == other.valueLogger and self.count == other.count and self.settings == other.settings

        def __reduce__(self):
            return (self.__class__, (self.valueLogger, self.settings))

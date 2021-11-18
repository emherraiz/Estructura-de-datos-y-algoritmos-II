from SerVivo import SerVivo



class Guerrero(SerVivo):
    __max_target = 10

    def __init__(self, name):
        SerVivo.__init__(self)

        self._target = self.__generateTargetToDie()
        self._name = name

        def get_name(self):
            return self._name
        
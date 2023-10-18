class Haydovchi:
    def __init__(self, name, finish_time) -> None:
        self._name = name
        self._finish_time = finish_time
        
    def getName(self):
        return self.name

    def getFinishingTime(self):
        return self._finish_time

    @property
    def name(self):
        return self._name
class GP:
    def __init__(self, name) -> None:
        self._name = name
        self.drivers = []
        
    def addDriver(self, driver):
        self.drivers.append(driver)
        
    def getGPRanking(self):
        return sorted(
            self.drivers,
            key=lambda x: x.getGPPoints(),
            reverse=True)
    
    @property
    def name(self):
        return self._name
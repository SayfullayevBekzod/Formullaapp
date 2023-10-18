from haydovchi import Haydovchi
from gp import GP

class Championship:

    def __init__(self) -> None:
        self.driver_list: list[Haydovchi] = []
        self.gp_list: list[GP] = []

    def defineGrandPrix(self, name):
        gp = GP(name)
        self.gp_list.append(gp)
        return gp

    def getGrandPrix(self, name):
        for gp in self.gp_list:
            if gp.name == name:
                return gp
        return None

    def createDriver(self, name):
        driver = Haydovchi(name)
        self.driver_list.append(driver)
        print('qo\'shildi')
        return driver

    def getDrivers(self):
        return self.driver_list

    def getDriver(self, name):
        for driver in self.driver_list:
            if driver.name == name:
                return driver
        return None
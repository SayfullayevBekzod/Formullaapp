from haydovchi import Haydovchi
from gp import GP
from time1 import Time, TugashVaqti

class Championship:

    def __init__(self) -> None:
        self.driver_list: list[Haydovchi] = []
        self.driver_time_list: list[Time] = []
        self.gp_list: list[GP] = []

    def add_gpdriver(self, gp: GP, driver: Haydovchi, tugash_vaqti: TugashVaqti):
        for _gp in self.gp_list:
            if gp.name == _gp.name:
                driver.set_end_time(tugash_vaqti)
                _gp.collect_driver(driver)

    def set_time(self, gp: GP, driver: Haydovchi, tugash_vaqti: TugashVaqti):
        driver.set_gp(gp)
        time = Time(gp, driver, tugash_vaqti)
        self.add_gpdriver(gp, driver, tugash_vaqti)
        self.driver_time_list.append(time)
        return time

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
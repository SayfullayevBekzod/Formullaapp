from driver import Driver
from gp import Gp
from time1 import Time, TugashVaqti
class Chempionship:
    def __init__(self) -> None:
        self._drivers = []
        self._gps = []
        
    def createGriver(self, name):
        self._new_driver = Driver(name)
        self._drivers.append(self._new_driver)
        return self._new_driver
    
    def get_drivers(self):
        return self._drivers
    
    def get_driver(self, name):
        for driver in self._drivers:
            if name == driver.get_name:
                return driver
        return None
    
    def define_gp(self, name):
        self._new_gp = Gp(name)
        self._gps.append(self._new_gp)
        return self._new_gp
    
    def get_gp(self, name):
        for gps in self._gps:
            if name == gps.get_name:
                return gps
        return "Bunday Grand Pri yo'q"
    
    def enter_driver(self, gp, driver:Driver):
        for gps in self._gps:
            if gps == gp:
                gps.enter_driver(driver)
                return "Nimadir"
        return "hishnima"
    
    def gp_ranking(self, gp: Gp):
        for gps in self._gps:
            if gps == gp:
                return gps.get_ranking()
        return -1.0
    
    def get_position(self, driver: Driver, gp: Gp):
        for gps in self._gps:
            if gps == gp:
                return gps.get_position()
        return -1.0
    
    def add_position(self, dr: Driver, gp: Gp):
        dr.get_races()[gp][0] = self.add_position(dr, gp)
        place = dr.add_races()[gp][0]
        if place == 1:
            dr.get_races()[gp][1] = 25
        elif place == 2:
            dr.get_races()[gp][1] = 18
        elif place == 3:
            dr.get_races()[gp][1] = 15
        elif place == 4:
            dr.get_races()[gp][1] = 12
        elif place == 5:
            dr.get_races()[gp][1] = 10
        elif place == 6:
            dr.get_races()[gp][1] = 8
        elif place == 7:
            dr.get_races()[gp][1] = 6
        elif place == 8:
            dr.get_races()[gp][1] = 4
        elif place == 9:
            dr.get_races()[gp][1] = 2
        elif place == 10:
            dr.get_races()[gp][1] = 1
            
    def get_championship_ranking(self):
        ranking = {}
        drs = self._drivers
        for i in range(len(self._drivers)):
            highest = -1
            highest_dr = None
            for dr in self._drivers:
                if dr.get_points() > highest:
                    highest = dr.get_points()
                    highest_dr = dr
            ranking.update({highest_dr.get_name: highest_dr.get_points()})
            drs.remove(highest_dr)
            drs.append(Driver("some"))
        return ranking
            
    def set_time(self, gp: Gp, driver: Driver, hour, minute, second, ms):
        for gps in self._gps:
            if gp == gps:
                finish_time = TugashVaqti(hour, minute, second, ms)
                for dr in gp.get_drivers():
                    if dr == driver:
                        gp.get_drivers()[driver][0] = finish_time
                        rank = 0
                        for dr2 in gp.get_drivers():
                            if dr2 != driver and  gp.get_drivers[dr][0] != 0:
                                rank += 1
                                if gp.get_drivers()[driver][0].get_hour < gp.get_drivers()[dr2][0].get_hour:
                                    gp.get_drivers()[driver][1], gp.get_drivers()[dr2][1] = gp.get_drivers()[dr2][1], gp.get_drivers()[dr2][1] + 1
                                    self.add_position(gp, driver)
                                    self.add_position(gp, dr2)
                                elif gp.get_drivers()[driver][0].get_hour == gp.get_drivers()[dr2][0].get_hour:
                                    if gp.get_drivers()[driver][0].minut < gp.get_drivers()[dr2][0].minut:
                                        gp.get_drivers()[driver][1], gp.get_drivers()[dr2][1] = gp.get_drivers()[dr2][1], gp.get_drivers()[dr2][ 1] + 1
                                        self.add_position(gp, driver)
                                        self.add_position(gp, dr2)
                                    elif gp.get_drivers()[driver][0].minute == gp.get_drivers()[dr2][0].minute:
                                        if gp.get_drivers()[driver][0].second < gp.get_drivers()[dr2][0].second:
                                            gp.get_drivers()[driver][1], gp.get_drivers()[dr2][1] = \
                                                gp.get_drivers()[dr2][
                                                    1], \
                                                gp.get_drivers()[dr2][
                                                    1] + 1
                                            self.add_position(gp, driver)
                                            self.add_position(gp, dr2)
                                        elif gp.get_drivers()[driver][0].second == gp.get_drivers()[dr2][
                                            0].second:
                                            if gp.get_drivers()[driver][0].ms < gp.get_drivers()[dr2][
                                                0].ms:
                                                gp.get_drivers()[driver][1], gp.get_drivers()[dr2][1] = gp.get_drivers()[dr2][1],gp.get_drivers()[dr2][1] + 1
                                                self.add_position(gp, driver)
                                                self.add_position(gp, dr2)
                                            elif gp.get_drivers()[driver][0].ms == gp.get_drivers()[dr2][0].ms:
                                                gp.get_drivers()[driver][1] = gp.get_drivers()[dr2][1]
                                                self.add_position(gp, driver)
                                                self.add_position(gp, dr2)
                                            else:
                                                gp.get_drivers()[driver][1] = gp.get_drivers()[dr2][1] + 1
                                                self.add_position(gp, driver)
                                                self.add_position(gp, dr2)
                                        else:
                                            gp.get_drivers()[driver][1] = gp.get_drivers()[dr2][1] + 1
                                            self.add_position(gp, driver)
                                            self.add_position(gp, dr2)
                                    else:
                                        gp.get_drivers()[driver][1] = gp.get_drivers()[dr2][1] + 1
                                        self.add_position(gp, driver)
                                        self.add_position(gp, dr2)
                                else:
                                    gp.get_drivers()[driver][1] = gp.get_drivers()[dr2][1] + 1
                                    self.add_position(gp, driver)
                                    self.add_position(gp, dr2)
                        if rank == 0:
                            gp.get_drivers()[driver][1] = 1
                            self.add_position(gp, driver)
                            return finish_time
                        else:
                            return finish_time
                return "No such driver"
        return "No such Grand Pri"

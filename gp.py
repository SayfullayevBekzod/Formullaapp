from driver import Driver
from time1 import Time, TugashVaqti
class Gp:
    def __init__(self, name) -> None:
        self._name = name
        self._drivers = {}
        
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def get_name(self, new_name):
        self._name = new_name
        
    
    def enter_driver(self, driver: Driver):
        self._drivers.update({driver: [TugashVaqti(00, 00, 00, 0000), 0]})
        
    def get_drivers(self):
        return self._drivers
    
    def get_ranking(self):
        ultimate_lst = []
        for i in range(len(self._drivers)):
            for dr in self._drivers:
                if self._drivers[dr][1] != 0:
                    if self._drivers[dr][1] == i + 1:
                        ultimate_lst.append({dr.get_name:[self._drivers[dr][0].to_string(), self._drivers[dr][0]]})
                else:
                    ultimate_lst.insert(len(self._drivers) - 1, {dr.get_name: [self._drivers[dr][0].to_string(), self._drivers[dr][1]]})
        return ultimate_lst
    def get_position(self, driver:Driver):
        for dr in self._drivers:
            if dr == driver:
                return self._drivers[dr][1]
        return 'no such driver'
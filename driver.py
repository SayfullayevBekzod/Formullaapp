class Driver:
    def __init__(self, name):
        self._name = name
        self._races = {}
        
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def get_name(self, new_name):
        self._name = new_name
        
    def add_race(self, gp):
        self._races.update({gp:[0,0]})
        
    def get_raced(self):
        return self._races.keys()
    
    def get_races(self):
        return self._races
    
    def get_points(self):
        points = 0
        for lst in self._races.keys():
            points += lst[1]
        return points
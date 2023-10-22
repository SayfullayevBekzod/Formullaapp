# from haydovchi import Haydovchi

class GP:
    ball = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9:2, 10:1}
    def __init__(self, name) -> None:
        self._driver_list = []
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def collect_driver(self, driver):
        self._driver_list.append(driver)
        print('gp ga qo\'shildi')


    def get_gp_ranking(self):
        full_data = {}
        for haydovchi in self._driver_list:
            full_data[haydovchi.name] = haydovchi.endtime
        res = list(sorted(full_data, reverse=True))
        return res
    
    def get_position(self, driver):
        position = 0
        list_result = self.get_gp_ranking()
        for i in list_result:
            if i == driver.name:
                position += 1
                return position
            else:
                position += 1
        return None
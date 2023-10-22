class Haydovchi:
    def __init__(self, name) -> None:
        self._name = name
        self.endtime = None
        self.gp_list = []
        self.ball = 0

    @property
    def name(self):
        return self._name
    
    def set_end_time(self, time):
        self.endtime = time._hour * 3600000 + time._minut * 60000 + time._second * 1000 + time._ms
        print('haydovchiga vaqti berildi')
        # print(f"test {self.endtime}")

    def set_gp(self, gp):
        print(self.gp_list)
        self.gp_list.append(gp.name)
        print(self.gp_list)

    def get_raced(self):
        return self.gp_list
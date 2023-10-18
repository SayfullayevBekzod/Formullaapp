from championship import Championship
from haydovchi import Haydovchi
from gp import GP
from time1 import Time

chempionat = Championship()
time = Time()
time.setTime(1, 30, 45, 500)
print(time)  # Soat:minut:soniya.millisikund formatida vaqtni chiqaradi


chempionat1 = Haydovchi("Ali",120)
chempionat2 = Haydovchi("Alijon", 130)
chempionat3 = Haydovchi("Vali", 150)
chempionat4 = Haydovchi("Qodir", 100)
print(f"{chempionat1.getName()} --> {chempionat1.getFinishingTime()}")
print(f"{chempionat2.getName()} --> {chempionat2.getFinishingTime()}")
print(f"{chempionat3.getName()} --> {chempionat3.getFinishingTime()}")
print(f"{chempionat4.getName()} --> {chempionat4.getFinishingTime()}")
print(chempionat4._finish_time)

# print(chempionat.defineGrandPrix('katta aylana yo\'li'))
# print(chempionat.getGrandPrix('kattaaylana yo\'li'))

#chempionat.createDriver('ibrohimjon')
#chempionat.createDriver('ali')
#print(chempionat.getDriver('ali'))
#print(chempionat.getDrivers())
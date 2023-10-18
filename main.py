from championship import Championship
from haydovchi import Haydovchi
from time1 import Time
from gp import GP

chempionat = Championship()
chempionat1 = Haydovchi("Ali", 10)
chempionat1 = Haydovchi("Alijon", 9)
chempionat1 = Haydovchi("Ali", 8)
chempionat1 = Haydovchi("Ali", 7)
chempionat2 = GP("Ali")
print(chempionat2.getGPRanking())
# print(chempionat.defineGrandPrix('katta aylana yo\'li'))
# print(chempionat.getGrandPrix('kattaaylana yo\'li'))

#chempionat.createDriver('ibrohimjon')
#chempionat.createDriver('ali')
#print(chempionat.getDriver('ali'))
#print(chempionat.getDrivers())
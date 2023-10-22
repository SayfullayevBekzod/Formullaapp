from championship import Championship
from gp import GP
from haydovchi import Haydovchi
from time1 import TugashVaqti

chempionat = Championship()

chempionat.defineGrandPrix("katta halqa")
gp = GP("katta halqa")
gp1 = GP("tekis yolak")
driver1 = Haydovchi('ali')
driver2 = Haydovchi('vali')

tugash_vaqti1 = TugashVaqti(11, 35, 34, 123)
tugash_vaqti2 = TugashVaqti(11, 35, 34, 122)
tugash_vaqti3 = TugashVaqti(11, 35, 34, 120)


print(chempionat.set_time(gp, driver1, tugash_vaqti1))
print(chempionat.set_time(gp, driver2, tugash_vaqti2))
print(chempionat.set_time(gp1, driver1, tugash_vaqti3))

a = chempionat.getGrandPrix("katta halqa")
print(a.get_gp_ranking())
print(a.get_position(driver1))
print(driver1.get_raced())

# print(chempionat.defineGrandPrix('katta aylana yo\'li'))
# print(chempionat.getGrandPrix('kattaaylana yo\'li'))

# chempionat.createDriver('ibrohimjon')
# chempionat.createDriver('ali')
# print(chempionat.getDriver('ali'))
# print(chempionat.getDrivers())
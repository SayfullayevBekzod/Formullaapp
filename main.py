from championship import Chempionship


tournament = Chempionship()

tournament.createGriver("Lewis Hamilton")
tournament.createGriver("Michael Schumacher")
tournament.createGriver("Sebastian Vettel")
tournament.createGriver("Alain Rost")

for d in tournament.get_drivers():
    print(d.get_name)

print()
dr = tournament.get_driver("Lewis Hamilton")
dr2 = tournament.get_driver("Michael Schumacher")
dr3 = tournament.get_driver("Sebastian Vettel")
dr4 = tournament.get_driver("Alain Rost")
if dr != -1.0:
    print(dr.get_name)

gp1 = tournament.define_gp("55th annual grand pri tournament")
print(tournament.define_gp("Mayor's Special Grand Pri Tournament"))

print(tournament.get_gp("Mayor's Special Grand Pri Tournament"))
print(tournament.get_gp("Formula-1"))

tournament.enter_driver(gp1, dr)
tournament.enter_driver(gp1, dr2)
tournament.enter_driver(gp1, dr3)
tournament.enter_driver(gp1, dr4)

print(tournament.set_time(dr, dr, 1, 20, 40, 50))
print(tournament.set_time(dr, dr2, 0, 40, 0, 0))
print(tournament.set_time(dr2, dr3, 0, 20, 0, 0))
print(tournament.set_time(dr3, dr4, 0, 15, 0, 0))

print(tournament.gp_ranking(dr))
print(tournament.get_position(dr3, gp1))

print(tournament.get_championship_ranking())


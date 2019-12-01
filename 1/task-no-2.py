f = open('input', "r")
all_mass = f.readlines()
all_fuel = 0
for mass in all_mass:
    fuel = int(mass)//3 -2
    while fuel>0:
        all_fuel += fuel
        fuel = fuel//3 -2
print(all_fuel)
f.close()
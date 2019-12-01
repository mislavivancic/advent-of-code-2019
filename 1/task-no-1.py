f = open('input', "r")
print(sum([(int(mass)//3 -2) for mass in f.readlines()]))
f.close()
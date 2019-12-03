import numpy as np
f = open("input","r")
path1 = f.readline().split(",")
path2 = f.readline().split(",")
print(len(path1))
print(len(path2))

stops1 = [(0,0)]
stops2 = [(0,0)]
stop = False
i=0
for directionDistance in path1:
    direction = directionDistance[0]
    distance = int(directionDistance[1:])
    for j in range(distance):
        
        if direction == "R":
            stops1.append((stops1[i+j][0] + 1,stops1[i+j][1]))
        
        if direction == "L":
            stops1.append((stops1[i+j][0] - 1, stops1[i+j][1]))

        if direction == "U":
            stops1.append((stops1[i+j][0], stops1[i+j][1] + 1))

        if direction == "D":
            stops1.append((stops1[i+j][0], stops1[i+j][1] - 1))

    i += j+1


i=0
for directionDistance in path2:
    direction = directionDistance[0]
    distance = int(directionDistance[1:])
    for j in range(distance):
        
        if direction == "R":
            stops2.append((stops2[i+j][0] + 1,stops2[i+j][1]))
        
        if direction == "L":
            stops2.append((stops2[i+j][0] - 1, stops2[i+j][1]))

        if direction == "U":
            stops2.append((stops2[i+j][0], stops2[i+j][1] + 1))

        if direction == "D":
            stops2.append((stops2[i+j][0], stops2[i+j][1] - 1))

    i += j+1

manhatan_distances = []
stops1 = stops1[1:]
stops2 = stops2[1:]

for stop1 in stops1:
    if stop1 in stops2:
        print(stop1)
        manhatan_distances.append(abs(stop1[0])+abs(stop1[1]))

print(min(manhatan_distances))
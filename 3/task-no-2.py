import numpy as np
import sys
f = open("input","r")
path1 = f.readline().split(",")
path2 = f.readline().split(",")

f2 = open("intersections","r")
intersections = []
intersections_unformated = f2.readlines()

for intersect in intersections_unformated:
    intersect = intersect[1:-2].split(",")
    intersections.append((int(intersect[0]),int(intersect[1])))


dict1 = {}

for intersect in intersections:
    dict1[intersect] = 0

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
        
        if stops1[-1] in intersections:
            dict1[stops1[-1]] = i+j+1

    i += j+1



dict2 = {}

for intersect in intersections:
    dict2[intersect] = 0
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

        if stops2[-1] in intersections:
            dict2[stops2[-1]] = i+j+1

    i += j+1


combined_steps = []

for intersect in dict1:
    combined_steps.append(dict1[intersect]+dict2[intersect])

print(min(combined_steps[:-1]))
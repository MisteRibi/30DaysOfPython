from conf import style
from math import sqrt # import square root from math module

def calcDist(p1,p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

pointA = (2,3)
pointB = (10,8)
distance = calcDist(pointA, pointB)

print(style.MAGENTA + "Euclidean distance between (2,3) and (10,8): " + style.RESET + str(distance))

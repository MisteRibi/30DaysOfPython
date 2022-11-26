from conf import style
from functions import calcDist # import square root from math module

pointA = (2,3)
pointB = (10,8)
distance = calcDist(pointA, pointB)

print(style.MAGENTA + "Euclidean distance between (2,3) and (10,8): " + style.RESET + str(distance))

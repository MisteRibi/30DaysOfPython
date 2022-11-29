from conf import style
from math import pi as pi

print(style.MAGENTA + 'Day 3')
"""
age = int(input(style.CYAN+'What\'s your age: '+style.RESET))
height = float(input(style.CYAN+'What\'s your height: '+style.RESET))
# 3. declare a variable that store a complex number?

# 4. script that ask base and height of triangle and calculate aera
print(style.MAGENTA+'\nArea of a triangle from base and height value.')
baseTriangle = float(input(style.CYAN+'What\'s the base size: '+style.RESET))
heightTriangle = float(input(style.CYAN+'What\'s the height size: '+style.RESET))
areaTriangle = 0.5 * baseTriangle * heightTriangle
print(style.CYAN+'The area of the triangle is: '+style.RESET,areaTriangle)

# 5. script ask all three side triangle and calcul perimeter
print(style.MAGENTA+'\nPerimeter of a triangle.')
sideATriangle = float(input(style.CYAN+'First side: '+style.RESET))
sideBTriangle = float(input(style.CYAN+'Second side: '+style.RESET))
sideCTriangle = float(input(style.CYAN+'Third side: '+style.RESET))
perimeterTriangle = sideATriangle + sideBTriangle + sideCTriangle
print(style.CYAN+'The perimter of the triangle is: '+style.RESET,perimeterTriangle)
"""

# 6. get lenght and width rectangle and calculate area and perimeter
print(style.MAGENTA+'\nArea and perimeter of a rectangle.')
lengthRect = float(input(style.CYAN+'Length of the rectangle: '+style.RESET))
widthRect = float(input(style.CYAN+'Width of the rectangle: '+style.RESET))
areaRect = lengthRect * widthRect
perimeterRect = 2 * (lengthRect + widthRect)
print(style.CYAN+'The area is:'+style.RESET, areaRect)
print(style.CYAN+'The perimiter is:'+style.RESET, perimeterRect)

# 7. get radius circle and calculate area and circumference
print(style.MAGENTA+'\nArea and circumference of a circle.')
radiusCircle = float(input(style.CYAN+'Radius of the circle: '+style.RESET))
areaCircle = pi * radiusCircle * radiusCircle
circumCircle = 2 * pi * radiusCircle
print(style.CYAN+'The area is:'+style.RESET, areaCircle)
print(style.CYAN+'The circumference is:'+style.RESET, circumCircle)

# 8. Calculate the slope, x-intercept and y-intercep of y = 2x -2


# 9. Slope is ( m = y2-y1/x2-x1). 
# Find the slope and Euclidean distance between point (2,2) and point (6,10)


# 10. Compare the slopes in tasks 8 and 9.


# 11. Calculate the value of y ( y = x^2 + 6x + 9).
# Try to use different x values and figure out at what x value y is going to be 0.

# 12. Find the lenght of 'python' and 'dragon' and make a falsy comparision statement.
print(style.MAGENTA+'\nComparing the length of the words python and dragon.')
print(style.CYAN+'Does the length of python and dragon are the same?'+style.RESET, not (len('python') == len('dragon')))

# 13. Use and operator to check if 'on' is found on both 'python' and 'dragon'.
print(style.CYAN+'Does \"on\" exist in both python and dragon?'+style.RESET, 'on' in 'python' and 'on' in 'dragon')
# 14.
print(style.CYAN+'Is \"jargon\" inside the sentence \"I hope this course isn\'t full of jaron.\"?'+style.RESET, 'jargon' in 'I hope this course isn\'t full of jargon.')
# 15.
print(style.CYAN+'Is there no \"on\" in both dragon and python?'+style.RESET, not ('on' in 'dragon' and 'on' in 'python'))





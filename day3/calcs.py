from conf import style as s
from math import pi as pi

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
def triangle1():
    print(s.MAGENTA+'\nArea of a triangle from base and height value.')
    baseTriangle = float(input(s.CYAN+'What\'s the base size: '+s.RESET))
    heightTriangle = float(input(s.CYAN+'What\'s the height size: '+s.RESET))
    areaTriangle = 0.5 * baseTriangle * heightTriangle
    print(s.CYAN+'The area of the triangle is: '+s.RESET,areaTriangle)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
def triangle2():
    print(s.MAGENTA+'\nPerimeter of a triangle.')
    sideATriangle = float(input(s.CYAN+'First side: '+s.RESET))
    sideBTriangle = float(input(s.CYAN+'Second side: '+s.RESET))
    sideCTriangle = float(input(s.CYAN+'Third side: '+s.RESET))
    perimeterTriangle = sideATriangle + sideBTriangle + sideCTriangle
    print(s.CYAN+'The perimter of the triangle is: '+s.RESET,perimeterTriangle)
    
# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
def rect():
    print(s.MAGENTA+'\nArea and perimeter of a rectangle.')
    lengthRect = float(input(s.CYAN+'Length of the rectangle: '+s.RESET))
    widthRect = float(input(s.CYAN+'Width of the rectangle: '+s.RESET))
    areaRect = lengthRect * widthRect
    perimeterRect = 2 * (lengthRect + widthRect)
    print(s.CYAN+'The area is:'+s.RESET, areaRect)
    print(s.CYAN+'The perimiter is:'+s.RESET, perimeterRect)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
def circle():
    print(s.MAGENTA+'\nArea and circumference of a circle.')
    radiusCircle = float(input(s.CYAN+'Radius of the circle: '+s.RESET))
    areaCircle = pi * radiusCircle * radiusCircle
    circumCircle = 2 * pi * radiusCircle
    print(s.CYAN+'The area is:'+s.RESET, areaCircle)
    print(s.CYAN+'The circumference is:'+s.RESET, circumCircle)








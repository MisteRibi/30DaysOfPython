from conf import style
from level1 import *
import math

print(style.MAGENTA + 'Point 1: ')
print(style.CYAN + 'Type of var firstName: ' + style.RESET , type(firstName))
print(style.CYAN + 'Type of var lastName: ' + style.RESET , type(lastName))
print(style.CYAN + 'Type of var fullName: ' + style.RESET , type(fullName))
print(style.CYAN + 'Type of var country: ' + style.RESET , type(country))
print(style.CYAN + 'Type of var city: ' + style.RESET , type(city))
print(style.CYAN + 'Type of var age: ' + style.RESET , type(age))
print(style.CYAN + 'Type of var year: ' + style.RESET , type(year))
print(style.CYAN + 'Type of var isMarried: ' + style.RESET , type(isMarried))
print(style.CYAN + 'Type of var isTrue: ' + style.RESET , type(isTrue))
print(style.CYAN + 'Type of var isLightOn: ' + style.RESET , type(isLightOn)) 
print(style.CYAN + 'Type of var birthMonth: ' + style.RESET , type(birthMonth))
print(style.CYAN + 'Type of var birthDay: ' + style.RESET , type(birthDay))
print(style.CYAN + 'Type of var birthYeat: ' + style.RESET , type(birthYear))

print(style.MAGENTA + '\nPoint 2: ')
print(style.CYAN + 'The length of firstName: ' + style.RESET, len(firstName))
print(style.MAGENTA + '\nPoint 3: ')
if firstName == lastName:
    print(style.CYAN + 'Compared the length of firstName and lastName: ' + style.RESET + "they are the same.")
elif firstName > lastName:
    print(style.CYAN + 'Compared the length of firstName and lastName: ' + style.RESET + "firstName is greater than lastName.")
elif firstName < lastName:
    print(style.CYAN + 'Compared the length of firstName and lastName: ' + style.RESET + "firstName is less than lastName.")

print(style.MAGENTA + '\nPoint 4: ')
numOne, numTwo = 5, 4
print(style.CYAN + 'There is two numbers set: ' + style.RESET, numOne, ' and ', numTwo)
total = numOne + numTwo
print(style.CYAN + 'The total of the two numbers is: ' + style.RESET, total)
diff = numTwo - numOne
print(style.CYAN + 'The difference between the two numbers is: ' + style.RESET, diff)
product = numTwo * numOne
print(style.CYAN + 'The product of the two numbers is: ' + style.RESET, product)
division = numOne/numTwo
print(style.CYAN + 'The division of the two numbers is: ' + style.RESET, division)
remainder = numTwo%numOne
print(style.CYAN + 'The remainder of the two numbers is: ' + style.RESET, remainder)
exp = numOne**numTwo
print(style.CYAN + 'The result of first number exponent the second number is: ' + style.RESET, exp)
floorDivision = numOne//numTwo
print(style.CYAN + 'The floor division of the two number is: ' + style.RESET, floorDivision)

print(style.MAGENTA + '\nPoint 5:')
radius = 30
print(style.CYAN + 'The radius of the circle is: ' + style.RESET, radius)
areaCircle = math.pi * radius**2
print(style.CYAN + 'The area of the circle is: ' + style.RESET, areaCircle)
circumCircle = 2 * math.pi * radius
print(style.CYAN + 'The circumference of the circle is: ' + style.RESET, circumCircle)
# would like to add a try and except to accept only numbers.
radiusUser = int(input(style.CYAN + 'Which radius do you want to find the area and the circumference of? ' + style.RESET))
areaCircleUser = math.pi * radiusUser**2
circumCircleUser = 2 * math.pi * radiusUser
print(style.CYAN + f'The area of the circle is {style.RESET}{areaCircleUser}{style.CYAN} and the circumference is {style.RESET}{circumCircleUser}{style.CYAN}.')

print(style.MAGENTA + '\nPoint 6:')
firstNameUser = input(style.CYAN + 'What is you first name: ' + style.RESET)
lastNameUser = input(style.CYAN + 'What is your last name: ' + style.RESET)
countryUser = input(style.CYAN + 'What is your country: ' + style.RESET)
ageUser = int(input(style.CYAN + 'Wath is you age: ' + style.RESET))
print(style.CYAN + f"Your name is {style.RESET}{firstNameUser} {lastNameUser}{style.CYAN}, your country is {style.RESET}{countryUser}{style.CYAN} and your age is {style.RESET}{ageUser}{style.CYAN}.")

print(style.MAGENTA + '\nPoint 7:')
import keyword
print(style.CYAN + f"Python have {style.RESET}{len(keyword.kwlist)}{style.CYAN} reserved word and they are: {style.RESET}{keyword.kwlist}")



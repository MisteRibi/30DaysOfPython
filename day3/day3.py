from conf import style as s
import calcs

print(s.MAGENTA+"Day 3: Operators")
print(s.CYAN+"""
      # 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle.
      Calculate the area of a triangle with the values of it's base and height.
      # 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle.
      Calculate the perimeter of a triangle with the values of the tree sides.
      # 6. Get length and width of a rectangle using prompt. Calculate its area and perimeter.
      Calculate the area and the perimeter of a rectangle with it's length and width values.
      # 7. Get radius of a circle using prompt. Calculate the area and circumference.
      Calculate the area and the circumference of a circle from it's radius value.
      """)
while True:
    try:
        userChoice = int(input(s.MAGENTA+"\nWhat do you want to do? "+s.RESET))
    except ValueError:
        print(s.RED+"\nOnly numbers please :)")
    else:
        if userChoice == 4:
            calcs.triangle1()
        elif userChoice == 5:
            calcs.triangle2()
        elif userChoice == 6:
            calcs.rect()
        elif userChoice == 7:
            calcs.circle()
        elif userChoice == 0:
            print(s.GREEN+"Thanks.\nCreated by Jay with "+"\u2764\uFE0F")
            exit()
        else:
            print("Not avalaible")
    






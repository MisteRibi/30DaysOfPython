import sys
import os

os.system=""
class style():
    MAGENTA='\033[35m'
    CYAN='\033[36m'
    RESET='\033[0m'

print(style.MAGENTA + "Question 1:")
print(style.CYAN + "Python version: " + style.RESET + str(sys.version) + style.CYAN + "\nVersion info: " + style.RESET + str(sys.version_info))

print(style.MAGENTA + "\nQuestion 2:")
print(style.CYAN + "Addition 3 and 4: " + style.RESET + str(3 + 4))
print(style.CYAN + "Substraction 3 and: " + style.RESET + str(3 - 4))
print(style.CYAN + "Multiplication 3 and 4: " + style.RESET + str(3 * 4))
print(style.CYAN + "Modulus 3 and 4: " + style.RESET + str(3 % 4))
print(style.CYAN + "Division 3 and 4: " + style.RESET + str(3 / 4))
print(style.CYAN + "Exponential 3 and 4: " + style.RESET + str(3 ** 4))
print(style.CYAN + "Floor division operator 3 and 4: " + style.RESET + str(3 // 4))

print(style.MAGENTA + "\nQuestion 3:")
#print(style.CYAN + "First name: " + style.RESET + "Jérémy")
firstName = input(style.CYAN + "First name: " + style.RESET)
#print(style.CYAN + "Last name: " + style.RESET + "Libion")
lastName = input(style.CYAN + "Last name: " + style.RESET)
#print(style.CYAN + "Country: " + style.RESET + "Canada")
country = input(style.CYAN + "Country: " + style.RESET)
print("I'm enjoying 30 days of python")

print(style.MAGENTA + "\nQuestion 4:")
print(style.CYAN + 'Type of "10": ' + style.RESET + str(type(10)))
print(style.CYAN + 'Type of "9.8": ' + style.RESET + str(type(9.8)))
print(style.CYAN + 'Type of "3.14": ' + style.RESET + str(type(3.14)))
print(style.CYAN + 'Type of "4 - 4j": ' + style.RESET + str(type(4 - 4j)))
print(style.CYAN + 'Type of \"[\'Asabeneh\',\'Python\',\'Filand\']\": ' + style.RESET + str(type(['Asabeneh','Python','Finland'])))
print(style.CYAN + 'Type of "First name": ' + style.RESET + str(type(firstName)))
print(style.CYAN + 'Type of "Last name": ' + style.RESET + str(type(lastName)))
print(style.CYAN + 'Type of "Country": ' + style.RESET + str(type(country)))

from conf import style

# variables
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

print(style.CYAN + 'First name:'+ style.RESET, first_name)
print(style.CYAN + 'First name length:'+ style.RESET, len(first_name))
print(style.CYAN + 'Last name: '+ style.RESET, last_name)
print(style.CYAN + 'Last name length: '+ style.RESET, len(last_name))
print(style.CYAN + 'Country: '+ style.RESET, country)
print(style.CYAN + 'City: '+ style.RESET, city)
print(style.CYAN + 'Age: '+ style.RESET, age)
print(style.CYAN + 'Married: '+ style.RESET, is_married)
print(style.CYAN + 'Skills: '+ style.RESET, skills)
print(style.CYAN + 'Person information: '+ style.RESET, person_info)

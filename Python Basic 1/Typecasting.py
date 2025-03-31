# Typecasting = the process of converting a variable from one data type to another
               # str(), int(), float(),bool()
from variables import is_student

name = "krish kotadia"
age = 18
gpa = 9.9
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(age)
print(type(age))

name = bool(name)
print(name)  #will only be false if the name is left empty
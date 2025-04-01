# input() = A function that prompts the user to enter data
# Returns the entered data as a string


name = input("What is your name?: ")
age = input("How old are you?: ")

age = int(age)
#Another way is to typecast it into function i.e(line6) age = int(input(...
age = age +1
print("Happy birthday")
print(f"You are {age} years old")

print(f"Hello {name}!")

name = input("Enter your full name")

result = len(name)
print(result) #includes spaces

find = name.find(" ")
print(find) #gives index of a character

search = name.rfind("o")
print(search) #reverse order of index

name = name.capitalize()

name = name.upper()
name = name.lower()

inspect =  name.isdigit()
print(inspect) #search for only digits

inspect1 = name.isalpha() #if a string contains only alphabets
print(inspect1)


phoneno = input("Enter your number")

no = phoneno.count("-")
print(no)#counts characters


phoneno = phoneno.replace("-", " $ ")
print(phoneno)


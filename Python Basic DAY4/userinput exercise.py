username  = input("Enter  a username: ")



if len(username)>12:
    print("Cannot exceed 12 characters")

elif  not username.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not username.isalpha() :
    print("Cannot contain nos")
else:

    print(f"Weclome {username}")

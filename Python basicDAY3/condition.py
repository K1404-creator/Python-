age = int(input("Enter your age: "))

if age >= 100:
    print("Surpassed Expiry date")


elif age < 0 :
    print("error")

elif age>=18:
    print("adult")

else:
    print("minor")

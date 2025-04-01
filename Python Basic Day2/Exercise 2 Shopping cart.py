item = str(input("what item would you like to buy"))
price = float(input("What is the price"))
quantity =  int(input("How many items are you buying"))

total = price*quantity

print(f" you have bought {quantity} x {item}/s and your total is {total}")
# or and not
# or: atleast one condition must be true
# and both conditions must be true
# not inverts the condition (not false, not true)


temp = 34
is_raining = False


if temp > 40 or temp < 0 or is_raining:
    print(f"Outdoor event is cancelled")

else:
    print("The outdoor event is scheduled")



football = 34

is_sale = True

if football >=37 and is_sale:
    print("In stock")
elif football<0 and is_sale:
    print("Debt")
elif 26 > football > 20 and is_sale:
    print("Schedule order for later")
elif football >=33 and not is_sale:
    print("In stock")
elif football<0 and not is_sale:
    print("Debt")
elif 26 > football > 20 and not is_sale:
    print("Schedule order for later")
else:
    print("Reorder the stock")



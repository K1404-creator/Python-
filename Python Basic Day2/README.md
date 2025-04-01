README.md
Markdown
# Python Learning Repository

Welcome to the Python Learning Repository! This repository contains various exercises and examples to help you learn and practice Python programming.

## Repository Structure

This repository is organized into several exercises. Below is a brief description of the key files:

### Files

1. **Exercise 1: Rectangle Area Calculation**
   - **File:** `Python Basic Day2/Exercise1 Rectangle area.py`
   - **Description:** This script calculates the area of a rectangle. It prompts the user to input the length and breadth of the rectangle and then computes the area using the formula: `area = length * breadth`.

   ```python
   length = float(input("Enter length"))
   breadth = float(input("Enter breadth"))

   area = length * breadth

   print(f"area of the rectangle is: {area}")
Exercise 2: Shopping Cart

File: Python Basic Day2/Exercise 2 Shopping cart.py
Description: This script simulates a shopping cart. Users can add items to the cart, specify the price and quantity, and get the total cost.
Python
item = str(input("what item would you like to buy"))
price = float(input("What is the price"))
quantity = int(input("How many items are you buying"))

total = price * quantity

print(f" you have bought {quantity} x {item}/s and your total is {total}")
User Input Example

File: Python Basic Day2/userinput.py
Description: This script demonstrates how to take user input and process it. It includes examples of different types of user inputs and how to handle them.
Python
# input() = A function that prompts the user to enter data
# Returns the entered data as a string

name = input("What is your name?: ")
age = input("How old are you?: ")

age = int(age)
#Another way is to typecast it into function i.e(line6) age = int(input(...
age = age + 1
print("Happy birthday")
print(f"You are {age} years old")

print(f"Hello {name}!")
How to Run the Scripts
Clone the repository:

bash
git clone https://github.com/K1404-creator/Python-.git
cd Python-
Navigate to the desired exercise directory:

bash
cd "Python Basic Day2"
Run the scripts:

For Rectangle Area Calculation:
bash
python "Exercise1 Rectangle area.py"
For Shopping Cart:
bash
python "Exercise 2 Shopping cart.py"
For User Input Example:
bash
python "userinput.py"
Follow the on-screen prompts to enter the required values.

Contributing
Feel free to fork this repository, make your changes, and submit a pull request. Contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.

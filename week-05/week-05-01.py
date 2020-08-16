# Monday: Creating and calling functions

# def       printName       (name)      :
# keyword   Function Name   Parameters  Ending colon

from os import system
clear = lambda: system('clear')

clear() # use it to clear the terminal output

# writing your first function
def printInfo():        # defines what the function does when called
    print('Name: John Smith')
    print('Age: 45')

printInfo()             # calls the function to run
printInfo()             # calls the function again

# performing a calculation in a function
def calc():
    x, y = 5, 10
    print(x + y)

calc()  # will run the block of code within calc and output 15

# Monday Exercises

# Print Name
def myName():
    name = 'Michel Caraballo'
    print(name)

myName()

# Pizza Toppings
def pizzaToppings():
    toppings = ['Pepper Green', 'Pineapple', 'Mozzarella', 'Blue Cheese', 'Pepperonie']
    print('-'.join(toppings))

for i in range(3):
    pizzaToppings()
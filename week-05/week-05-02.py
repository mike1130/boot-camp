# Tuesday: Parameters
from os import system
clear = lambda: system('clear')

clear ()    # use it to clear the terminal output

# passing a single parameter into a function
def printName(full_name):
    print('Your name is: {}'.format(full_name))

printName('John Smith')
printName('Amanda')

# passing multiple parameters into a funciton
def addNums(num1, num2):
    result = num1 + num2
    print('{} + {} = {}'.format(num1, num2, result))

addNums(5, 8)       # will output 13
addNums(3.5, 5.5)   # will output 9.0

# using a function to square all information
numbers1 = [2, 4, 5, 10]
numbers2 = [1, 3, 6]

def squares(nums):
    for num in nums:
        print(num ** 2)

squares(numbers1)
squares(numbers2)

# setting default parameter values
def calcArea(r, pi=3.14):   # default parameters MUST always go after non-default parameters
    area = pi * (r ** 2)
    print('Area: {}'.format(area))

calcArea(2)     # assuming radius is the value of 2

# setting default parameter values
def printName(first, last, middle=''):
    if middle:
        print('{} {} {}'.format(first, middle, last))
    else:
        print('{} {}'.format(first, last))

print('John','Smith')
print('John','Smith','Paul')    # will output with middle name

# explicity assigning values to parameters by referencing the name
def addNums(num1, num2):
    print(num2)
    print(num1)

addNums(5, num2 = 2.5)

# using *args paramater to take in a tuple of arbitrary values
def outputData(name, *args):
    print(type(args))
    for arg in args:
        print(arg)

outputData('John Smith', 5, True, 'Jess')

# using *kwargs parameter to take in a dictionary of arbitrary values
def outputData(**kwargs):
    print( type(kwargs))
    print(kwargs['name'])
    print(kwargs['num'])

outputData(name = 'John Smith', num = 5, b = True)

# Tuesday Exercises

# User Input
word = input('Input a word: ')

def firstUpper(variable):
    if variable[0][0] == variable[0][0].upper():
        print(True)
    else:
        print(False)

firstUpper(word)

# No Name
first = input('Input your first name: ').capitalize()
last = input('Input your last name: ').capitalize()

def noName(first='', last=''):
    if not first and not last:
        print('No name passed in')
    else:
        print('Name: {} {}'.format(first, last))

noName(first, last)
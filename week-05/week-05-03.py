# Wednesday: Return statement

from os import system
clear = lambda: system('clear')

clear()     # use it to clear the terminal output

# using return keyword to return the sum of two numbers

def addNums(num1, num2):
    return num1 + num2

num = addNums(5.5, 4.5)     # saves returned value into num
print(num)
print( addNums(10, 10))     # doesn't save returned value

# shorthand syntax using a ternary operator
def searchList(aList, element):
    return True if element in aList else False

result = searchList(['one', 2, 'three'], 2)      # result = True
print(result)

# Wednesday Exercises

# Full Name
first = input('Input your first name: ').capitalize()
last = input('Input your last name: ').capitalize()

def fullName(first, last):
    return first + ' ' + last

full = fullName(first, last)
print(full)

# User Input
def userInput():
    x = input('Write anything: ')
    return x

y = userInput()
print(y)
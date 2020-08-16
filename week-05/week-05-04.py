# Thursday: Scope

from os import system
clear = lambda: system('clear')

clear()     # use it to clear the terminal output

# where global variables can be accessed
# number = 5

# def scopeTest():
#     number += 1     # not accessible due to function level scope

# scopeTest()

# accessing variables defines in a function
def scopeTest():
    word = 'Function'
    return word

value = scopeTest()
print(value)

# changing list item values by index
sports = ['Baseball','Football','Hockey','Basketball']
def change(aList):
    aList[0] = 'Soccer'

print('Before altering: {}'.format(sports))
change(sports)
print('After altering: {}'.format(sports))

# Thursday Exercises

# Names
names = ['Bob', 'Rich', 'Amanda']
def changeValue(aList, name, index):
    aList[index] = name
    
print('Before altering: {}'.format(names))
changeValue(names, 'Bill', 1)
print('After altering: {}'.format(names))

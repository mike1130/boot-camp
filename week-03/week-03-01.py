# User Input & Type Converting

# accepting and outputting user input
# print( input("What's your name? "))

# saving what the user inputs
ans = input("What's your name? ")
print("Hello {}!".format(ans))

# how to check the data type of a variable
num = 5
print( type(num))

# converting a variable from one data type to another
num = '9'
num = int(num)      # re-declaring num to store an integer
print( type(num))   # checking type to make sure conversion worked

# converting data types
num1 = 7
print(f'\n {type(str(num1))}')     # Integer to String
print( type(float(num1)))       # Integer to Float

num2 = 7.6
print(f'\n {type(int(num2))}')     # Float to Integer

var = '8'
print(f'\n {type(int(var))}')      # String to Integer

bol = 'True'
print(f'\n {type(bool(bol))}')     # String to Boolean

bol1 = True
print(f'\n {type(int(bol1))}')     # Boolean to Integer

# working user input to perform calculations
ans = input('Type a number to add: ')
print(type(ans))        # default type is string, mus convert
result = 100 + int(ans)
print('100 + {} = {}'.format(ans, result))

# using the try and except blocks, use tab to indent where necessary
try:
    ans = float(input('Type a number to add: '))
    print('100 + {} = {}'.format(ans, 100 + ans))
except:
    print('You did not put in a valid number!')
# without try/except print statement would not get hit if error occurs
print('The program did not break')

# Monday Exercises

# Converting
x = 'True'
print(type(bool(x)))

# Sum of inputs
x1 = int(input('Enter a number: '))
x2 = int(input('Enter other number: '))
print('{} + {} = {}'.format(x1, x2, x1 + x2))

# Car information 
year = int(input('Enter the year of your car: '))
make = input('Enter who make your car: ')
model = input('Enter the model of your car: ')
color = input('Enter the color of your car: ')
print('{} {} {} {}'.format(year, color, make, model))
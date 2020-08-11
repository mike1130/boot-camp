# Tuesday: Variables

num1 = 5            # storing an integer into a variable
num2 = 8.4          # storing a float into a variable
print(num1, num2)   # you can print multiple items using commas

# storing a boolean into a variable
switch = True
print(switch)

# storing strings into a variable
name = 'John Smith'
fav_number = '9'
print(name, fav_number) #will print 9 next to the name

# using two variables to create another variable
result = num1 + num2
print(result)
print(type(result))

# adding, deleting, multiplying, dividing from a variable
result += 1     # same as saying result = result + 1
print(result)
result *= num1  # same as saying result = result * num1
print(result)

# defining a variable and overwiting it's value
name = 'John'
print(name)
name = 'Sam'
print(name)

# Tuesday Exercises
# Variable Output
x = 3
y = 10
result = x + y
print(f'{x} + {y} = {result}')

# Area Calculation
width = 245.54
height = 13.66
result = width * height
print(f"The area of a {width}'' x {height}'' rectangle is {result}''")
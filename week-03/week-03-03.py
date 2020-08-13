# Wednesday: Elif statement

# using the elif conditional statement
x, y = 5, 10
if x > y:
    print('x is greater')
elif x < y:
    print('x is less')

# checking more than one elif conditional statement
x, y = 5, 10
if x > y:
    print('x is greater')
elif x < y:
    print('x is less')
elif (x + 5) == y:
    print('equal')

# writing multiple contidionals within each other - multiple block levels
x, y, z = 5, 10, 5
if x > y:
    print('greater')
elif x <= y:
    if x == z:
        print('x is equal to z')        # resulting output
    elif x != z:
        print('x is not equal to z')    # won't get hit

# testing outpu of two if statements in a row thar are both true
x, y, z = 5, 10, 5
if x < y:
    print('x is less')

if x == z:
    print('x is equal')

# testing output of an if and elif statement that are both true
x, y, z = 5, 10, 5
if x < y:
    print('x is less')
elif x == z:
    print('x is equal to z')

# Wednesday Exercises

# Higher/Lower
x1 = int(input('Write a number: '))
if x1 > 100:
    print('{} is greater than 100'.format(x1))
elif x1 < 100:
    print('{} is lower than 100'.format(x1))

# Find the solution
x, y, = 5, 10
if x > y:
    print('greater')
elif x < y:
    print('lower')
# Thursday: Else statements 

# using an else statement
name = 'John'
if name == 'Jacob':
    print('Hello Jacob!')
else:
    print('Hello {}!'.format(name))

# writing a full conditional statement with if, elif, else
name = 'John'
if name[0] == 'A':
    print('Name starts with an A')
elif name[0] == 'B':
    print('Name starts with an B')
elif name[0] == 'J':
    print('Name starts with an J')
else:                               # covers all other possibilities
    print('Name starts with an {}'.format(name[0]))

# Thursday Exercises

# Fix the errors
name = 'John'
if name == 'Jack':
    print('Hello Jack')
else:
    print('Hello {}'.format(name))

# User input
time = int(input('Please, enter the time of day in military time. \n Example, 1100 = 11:00 AM\n: '))
if time < 1200:
    print('Good morning!')
elif time > 1200 and time < 1700:
    print('Good afternoon!')
else:
    print('Good evening')

age = input('Please enter your age: ')

try:
    age = int(age)
    if age > 0 and age <= 12:
        print('Kid')
    elif age >= 13 and age <= 19:
        print('Tennager')
    elif age >= 20 and age <= 30:
        print('Young Adult')
    elif age >= 31 and age <= 64:
        print('Tennager')
    elif age >= 64:
        print('Senior')
except:
    print('Error: Improper numbers used. Please try again.')
# Tuesday: Working with dictionaries

from os import system
clear = lambda: system('clear')
clear()         # use it to clean the terminal output

# adding new key/value pairs to a dictionary
car = {'year': 2018}
car['color'] = 'Blue'
print('Year: {} \t Color: {}'.format( car['year'], car['color']))

# updating a value for a key/value pair that already exists
car = {'year': 2018, 'color': 'Blue'}
car['color'] = 'Red'
print('Year: {}\t color: {}'.format( car['year'], car['color']))

# deleting a key/value pair from a dictionary
car = {'year': 2018, 'color': 'Blue'}
try:
    del car['year']
    print(car)
except:
    print('That key does not exist')

# looping over a dictionary via the keys
person = {'name': 'John', 'age': 26}
for key in person.keys():
    print(key)
    print( person[key])     # will output the value at the current key
print('-' * 10)
# looping over a dictionary via the values
person = {'name': 'John', 'age': 26}
for value in person.values():
    print(value)

# looping over a dictionary via the key/value pair
person = {'name': 'John', 'age': 26}
for key, value in person.items():
    print('{}: {}'.format(key, value))

# Tuesday Exercises

# User input
person = dict()     # empty dictionary 
name = input('Write down your name: ')
address = input('Write down your address: ')
cel_number = input('Write down your cellphone number: ')

person['name'] = name
person['address'] = address
person['cel_number'] = cel_number

for key, value in person.items():
    print('{}: {}'.format(key, value))

# Problem-solving
person = {'name': 'John Smith'}
print(person['name'])
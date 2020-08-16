# Monday: Dictionaries

from os import system
clear = lambda: system('clear')

clear()     # use it to clean the terminal output

# declaring a dictionary variable
empty = {}  # empty dictionary
person = {'name': 'John Smith'}       # dictionary with one key/value pair
customer = {
    'name': 'Morty',
    'age': 26
}                   # dictionary with two key/value pairs
print(customer)

# accessing dictionary information through keys
person = {'name': 'John'}
print( person['name'])      # access information through the key

# using the get method to access dictionary information
person = {'name': 'John'}
print( person.get('name'))      # retrieves value of name key as before
print( person.get('profession', 'Profession is not available.'))    # get is a secure way to retrieve information

# storing a list within a dictionary and accessing it
data = {'sports': ['baseball', 'football', 'hockey', 'soccer']}
print(data['sports'][0])    # first access the key, then the index

# improperly storing a list within a dictionary
sports = ['baseball', 'football', 'hockey', 'soccer']
try:
    sports_dict = dict(sports)      # will produce error, no key
except:
    print('No primary key to access')

# storing a dictionary within a list and accessing it
data = ['John', 'Dennis', {'name': 'Kirsten'}]
print( data[2])             # the dictionary is in index 2
print( data[2]['name'])     # first access the index, then access the key

# storing a dictionary within a dictionary and accessing it
data = {
    'team': 'Boston Red Sox',
    'wins': {'2018': 108, '2017': 93}
}
print( data['wins'])        # will output the dictionary within the wins key
print( data['wins']['2018'])    # first acces the wins jey, then the next key

# Monday Exercises

# User input
data = {}
name = input('Write your name: ')
age = int(input('Write your age: '))
data = {
    'name': name,
    'age': age
}
print('Your name is {}, and your age is {}'.format( data.get('name'), data.get('age')))

# Accesing Ingredients
pizza = {
    'ingredients': ['cheese', 'sausage', 'peppers']
}
for topping in pizza['ingredients']:
    print(topping)
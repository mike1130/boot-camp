# Tuesday: Attributes
from os import system
clear = lambda: system('clear')
clear()     # use it to clean the terminal output

# how to define a class attribute
class Car():
    sound = 'beep'      # all car objects will have this sound attribute and it's value
    color = 'red'       # all car objects will have this color attribute and it's value

ford = Car()
print(ford.color)       # known as 'dot syntax'

# changing the value of and attribute
class Car():
    sound = 'beep'
    color = 'red'

ford = Car()
print(ford.sound)       # will output 'beep'
ford.sound = 'honk'     # from now on the value of fords sound is honk
                        # this does not affect other instances
print(ford.sound)

# using the init method to give instances personalized attributes upon creation
class Car():
    def __init__(self, color):
        self.color = color      # sets the attribute color to the value passed in

ford = Car('Blue')      # instantiating a Car class with the color blue
print(ford.color)

# defining different values for multiple instances
class Car():
    def __init__(self, color, year):
        self.color = color      # sets the attribute color to the value passed in
        self.year = year

ford = Car('Blue', 2016)     # Create a car object with the color blue and year 2016
subaru = Car('Red', 2018)    # Create a car object with the color red and year 2018

print(ford.color, ford.year)
print(subaru.color, subaru.year)

# using and accessing global class attributes
class Car():
    sound = 'beep'      # global attribute, accessible through the class itself
    def __init__(self, color):
        self.color = 'Blue'     # instance specific attribute, not accessible through the class itself

print(Car.sound)
# print(Car.color)      # won't work, as color is only available to instances of the Car Class, noy the class itself

ford = Car('blue')
print(ford.sound, ford.color)   # color will work as this is an instance

# Tuesday Exercises

# Dogs
class Dogs():
    species = 'Canine'
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dogs('Sammi', 'Husky')
dog2 = Dogs('Casey', 'Chocolate Lab')

print(dog1.species, dog1.name, dog1.breed)
print(dog2.species, dog2.name, dog2.breed)

# User input
class Person():
    def __init__(self, name):
        self.name = name

name = input('Enter your name, please: ')
person1 = Person(name)
print('Hello {}'.format(person1.name))
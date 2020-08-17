# Monday: Creating and Instantiating a Class
from os import system
clear = lambda: system('clear')
clear()     # use it to clean the terminal output

# creating your first class
class Car():
    pass    # simply using as a placeholder until we add more code

# instantiating an object from a class
class Car():        # parens are optional here
    pass

ford = Car()        # creates an instance of the Car class and stores into the variable ford
print(ford)

# instantiating multiple objects from the same class
class Car():
    pass

ford = Car()
subaru = Car()          # creates another object from the car class
print( hash(ford))
print( hash(subaru))    # hash outputs a numerical representation of the location
                        # in memory for the variable

# Monday Exercises

# Animals
class Animals():
    pass

lion = Animals()
tiger = Animals()
print(hash(lion))
print(hash(tiger))

# Problem-solving
class Bus:
    pass
school_bus = Bus()
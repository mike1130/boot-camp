# Thursday: Inheritance
from os import system
clear = lambda: system('clear')

clear()     # use it to clean the terminal output

# inheriting a class and accessing the inherited method
class Animal():
    def makeSound(self):
        print('roar')

class Dog(Animal):      # inheriting Animal class
    species = 'Canine'

sam = Dog()
sam.makeSound()     # accessible through inheritance
lion = Animal()
# lion.species      # not accesible, inheritance does not work backwards

# using the super() method to declar inherited attributes
class Animal():
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, species, name):
        self.name = name
        super().__init__(species)       # using super to declare the species attribute defined in Animal

sam = Dog('Canine', 'Sammi')
print(sam.species)

# overriding methods defined in the superclass
class Animal():
    def makeSound(self):
        print('roar')

class Dog(Animal):
    def makeSound(self):
        print('bark')

sam, lion = Dog(), Animal()     # delcaring multiple vriables on a single line

sam.makeSound()     # overriding will call the makeSound method in Dog
lion.makeSound()    # no overriding occurs as Animal does not inherit anything

# how to inherit multiple classes
class Physics():
    gravity = 9.8

class Automobile():
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year    # declaring all attributes on one line

class Ford(Physics, Automobile):        # able to access Physics and Automobile attributes and methods
    def __init__(self, model, year):
        Automobile.__init__(self, 'Ford', model, year)      # super does not work with multiple

truck = Ford('F-150', 2018)
print(truck.gravity, truck.make)   # output both attributes

# Thursday Exercises

# Good Guys/ Bad Guys
class Characters():
    def __init__(self, name, team, height, weight):
        self.name, self.team, self.height, self.weight = name, team, height, weight

    def sayHello(self):
        return "Hello, my name is {} and I'm on the {} guys".format(self.name, self.team)

class goodPlayers(Characters):
    def __init__(self, name, height, weight):
        super().__init__(name, 'good', height, weight)

class badPlayers(Characters):
    def __init__(self, name, height, weight):
        super().__init__(name, 'bad', height, weight)

max_ = goodPlayers('Max', "5\'11", 183)
tony_ = badPlayers('Tony', "6\'3", 201)

print(max_.sayHello())
print(tony_.sayHello())
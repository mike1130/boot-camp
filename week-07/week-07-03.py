# Wednesday: Methods
from os import system
clear = lambda: system('clear')
clear()     # use it to clean the terminal output

# defining and calling our first class method
class Dog():
    def makeSound(self):
        print('bark')

sam = Dog()
sam.makeSound()

# using the self keyword to access attributes within class methods
class Dog():
    sound = 'bark'
    def makeSound(self):
        print(self.sound)   # self required to access attributes defined in the class

sam = Dog()
sam.makeSound()

# undersanding which methods are accessible via the class itself and class instances
class Dog():
    sound = 'bark'
    def makeSound(self):
        print(self.sound)

    def printInfo():
        print('I am a dog.')

Dog.printInfo()         # abe to run printInfo beacause it does not include self parameter

# Dog.makesound()       # would produce error, self is in reference to instances only

sam = Dog()
sam.makeSound()     # able to access, self can reference the instances of sam
# sam.printInfo()   # will produce error, instances require the self parameter to access methods

# writing methods that accept parameters
class Dog():
    def showAge(self, age):
        print(age)              # does not need self, age is referencing the parameter not an attribute

sam = Dog()
sam.showAge(6)      # passing the integer 6 as an argument ot be showAge method


# using methods to set or return attribute values, proper programming practice
class Dog():
    name = ''   # would normally use init method to declare, this is for testing purposes
    def setName(self, new_name):
        self.name = new_name    # declares the new value for the name attribute

    def getName(self):
        return self.name        # returns the value of the name attribute

sam = Dog()
sam.setName('Sammi')
print( sam.getName())   # prints the returned value of sel.name


# incrementing/decrementing attribute values with methods, best programming practice
class Dog():
    age = 5
    def happyBirthday(self):
        self.age += 1

sam = Dog()
sam.happyBirthday()     # calls method to increment value by one
print(sam.age)          # better practice use getter, this is for testing purposes


# calling a class method from another method
class Dog():
    age = 6
    def getAge(self):
        return self.age

    def printInfo(self):
        if self.getAge() < 10:      # need self to call other method for an instance
            print('Puppy!')

sam = Dog()
sam.printInfo()

# using magic methods
class Dog():
    def __str__(self):
        return 'This is a dog class'

sam = Dog()
print(sam)      # will print the return of the string magic method

# Wednesday Exercises

# Animals
class Animals():
    def __init__(self):
        species = ''

    def setSpecies(self, new_species):
        self.species = new_species

    def getSpecies(self):
        return self.species


lion = Animals()
lion.setSpecies('Feline')
print(lion.getSpecies())

# User Input
class Person():
    def __init__(self, name):
        self.name = name
        age = 0

    def setAge(self, new_age):
        self.age = new_age

    def getAge(self):
        return self.age


person1 = Person('Michel')
person1.setAge(input('What is your age?: '))

print('Hello {}, your are {} years old.'.format( person1.getName(), person1.getAge()))
# Wednesday: Working with strings

# using the addition operator without variables
name = 'John' + ' ' + 'Smith'
print(name)

# using the addition operator with variables
first_name = 'John'
last_name = 'Smith'
full_name = first_name + ' ' + last_name
print(full_name)

# injecting variables using the format method
name = 'John'
print('Hello {}'.format(name))
print('Hello {}, you are {} years old!'.format(name, 28))

# using the new f strings
name = 'John'
print(f'Hello {name}')

# one major difference between versions 2 & 3
name = 'John'
print('Hello, %s' % name)

# python 2 multiple variable formatting
first_name = 'John'
last_name = 'Smith'
print('Hello, %s %s' % (first_name, last_name)) 
    # surround the variables in parenthesis

# using indexes to print each element
word = 'Hello'
print(word[0])          # will output 'H'
print(word[1])          # will output 'e'
print(word[-1])         # will output 'o'

# slicing
print(word[0 : 2])      # will output 'He'
    # variable_name [start : stop : step]

print(word[0 : 5 : 2])  # will output 'Hlo'

# Wednesday Exercises
# Variable Injection
name = 'John'
print('{} {} {} {}'.format(23, 4.5, False, name))

# Fill in the Blanks
print("{}'s favorite sprots is {}".format('Michel', 'soccer'))
print('{} is working on {} programming'.format('Michel', 'string injection'))
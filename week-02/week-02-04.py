# Thursday: string manipulation

# using the title method to capitalize a string
name = 'john smith'
print(name.title())
print(name.lower())
print(name.upper())

# replacing an exclamation point with a period
words = 'Hello there!'
print(words.replace('!', '.'))

# finding the starting index of our searched term
s = 'Look over that way'
print(s.find('over'))

# removing white space with strip
name = '    john   '
print(name.strip())
print(name.lstrip())    # removing white left space 
print(name.rstrip())    # removing white right space

# convertin a string into a list of words
s = 'These words are separated by spaces'
print(s.split(' '))

# Thursday Exercises
# Uppercasing
s = 'uppercase'
print(s.upper())

# Strip symbols
s = '$$John Smith'
print(s.strip('$'))

# Reverse
word = 'Hello'
print(word[ : : -1]) # slicing 
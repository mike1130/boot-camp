# Tuesday: If statements

# using an if statement to only run code if the condition is met
x, y = 5, 10
if x < y:
    print('x is less than y')

# checking user input
ans = int(input("What is 5 + 5? "))
if ans == 10:
    print('You got it right!')

# using the keyword 'and' in an 'if statement'
x, y, z = 5, 10, 5
if x < y and z == 5:
    print('Both statements were true')

# using the keyword 'or' in an 'if statement'
x, y, z = 5, 10, 5
if x < y or x != z:
    print('One or both statements were true')

# using the keyword 'not' within an 'if statement'
flag = False
if not flag:    # same as saying if not true
    print('Flag is False')

# using the keyword 'in' within an 'if statement'
word = 'Baseball'
if 'b' in word:
    print('{} contains the character b'.format(word))

# using the keyword 'not in' within an 'if statement'
word = 'Baseball'
if 'x' in word:
    print('{} contains the character b'.format(word))

# Checking Inclusion - Part 1
sentence = input('1. Write a sentences: ')
if 'es' in sentence:
    print('{} contains the char es'.format(sentence))

# Checking Inclusion - Part 2
sentence = input('2. Write a sentence: ')
if sentence[len(sentence)-3::] == 'ing':
    print('{} contains the char ing'.format(sentence))

# Cheking Equality
word1 = input('Write a word: ')
word2 = input('Write other word: ')
if word1.lower() == word2.lower():
    print('{} is equal to {}'.format(word1, word2))

# Returning exponents
x = int(input('write a number: '))
if x < 10:
    print('{} squared is {}'.format(x, x ** 2))
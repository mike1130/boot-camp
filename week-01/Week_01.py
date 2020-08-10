#!/usr/bin/env python
# coding: utf-8

# # Week 01

# In[5]:


# This is python
print('Hello, buddy!')


# In[4]:


# This is the first line in the cell



# This is the fifth line in the cell


# # Guessing Game

# In[10]:


# Guessing game
from random import randint
from IPython.display import clear_output

guessed = False
number = randint(0, 100)
guesses = 0

while not guessed:
    ans = int(input('Try to guess the number I am thinking of!'))
    # use tab to indent
    guesses += 1
    clear_output()
    if ans == number:
        print('Congrats! You guessed it correctly.')
        # use tab twice to indent twice
        print('It took you {} guesses!'.format(guesses))
        break
    elif ans > number:
        print('The number is lower than what you guessed.')
    elif ans < number:
        print('The number is greater than what you guessed.')


# In[ ]:





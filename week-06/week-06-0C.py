# Challenge question
from os import system
clear = lambda: system('clear')

clear()     # use it to clean the terminal output

def palindrome(word):
    return True if word == word[::-1] else False


def main():
    word = input('Please, write down a word: ').lower()
    print('The word {} is palindrome: {}'.format(word, palindrome(word))

if __name__ == '__main__':
    main()
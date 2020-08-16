# Weekly Challenge
# Refactor Hangman

# import additional functions
from random import choice
from os import system
clear = lambda: system('clear')

def outputInfo(guesses, guessed, lives):
    # output game information
    hidden_word = ''.join(guesses)
    print('Your guessed letters: {}'.format(guessed))
    print('Word to guess: {}'.format(hidden_word))
    print('Lives: {}'.format(lives))


def gameStatus(word, lives, guesses):
    if lives <= 0:
        print('You lost all your lives, you lost!')
        return True
    elif word == ''.join(guesses):
        print('Congratulations, you guesses it correctly')
        return True

    return False


def letterGuesse(ans, word, guesses, guessed, lives):
    game_over = False 

    clear()      # clear all previous output
    if ans == 'quit':
        print('Thanks for playing!')
        game_over = True
    elif ans in word and ans not in guessed:   # check if letter in word
        print('You guessed correctly!')
        
        # create a loop to change underscore to proper letter
        for i in range( len(word)):
            if word[i] == ans:      # compares values at indexes
                guesses[i] = ans
    elif ans in guessed:
        print('You already guessed that. Try again.')
    else:
        lives -= 1
        print('Incorrect, you lost a life.')

    if ans not in guessed:
        guessed.append(ans)         # add ans to guessed list

    return guesses, guessed, lives, game_over


def main(word, guesses, guessed, lives, game_over):
    while not game_over:
        outputInfo(guesses, guessed, lives)

        ans = input('Type quit or guess a letter: ').lower()

        guesses, guessed, lives, game_over = letterGuesse(ans, word, guesses, guessed, lives)
        if not game_over:
            game_over = gameStatus(word, lives, guesses)


if __name__ == '__main__':

    # declare game variable
    words = ['tree', 'basket', 'chair', 'paper', 'python']
    word = choice(words)        # randomly chooses a word from words list
    guessed, lives, game_over = [], 7, False    # multi variable assignment

    # create a list of underscores to the length of the word
    guesses = ['_'] * len(word)

    main(word,  guesses, guessed, lives, game_over)

   


    


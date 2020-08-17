# Friday: Creating Blackjack
from os import system
clear = lambda: system('clear')
clear()     # use it to clean the terminal output

from random import randint      # allows us to get a random number

# create the blackjack class, which will hold all game methods and attributes
class Blackjack():
    def __init__(self):
        self.deck =[]       # set to an empty list
        self.suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        self.values = (2, 3, 4 ,5 ,6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

    # create a method that creates a deck of 52 cards, each card should be a tuple with a value and suit
    def makeDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append( (value, suit))    # ex: (7, 'Hearts')

    # method to pop a card from deck using random index value
    def pullCard(self):
        return self.deck.pop( randint(0, len(self.deck) - 1))


# create a class for the dealer and player objects
class Player():
    def __init__(self, name, currency):
        self.name = name
        self.hand = []
        self.currency = currency
    
    def getCurrency(self):
        return self.currency

    def setCurrency(self, amount, won):
        """ 
            Take in amount to be added or subtracted, the won parameter will
            handle wheter or not the player won and should be added or subtracted
        """
        if won:
            self.currency += amount
        elif not won:
            self.currency -= amount

    # take in a tuple and append it to the hand
    def addCard(self, card):
        self.hand.append(card)

    # if not dealer's turn then only show one of his cards, otherwise show all
    def showHand(self, dealer_start = True):
        print('\n{}'.format(self.name))
        print('=' * 10)
        for i in range( len(self.hand)):
            if self.name == 'Dealer' and i == 0 and dealer_start:
                print('- of -')     # hide first card
            else:
                card = self.hand[i]
                print('{} of {}'.format( card[0], card[1]))
        
        print('Total = {}'.format( self.calcHand(dealer_start)))

    # if not dealer's turn then only give back total of second card
    def calcHand(self, dealer_start = True):
        total = 0
        aces = 0        # caclulate aces afterwards
        card_values = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9,
                         10:10, 'J':10, 'Q':10, 'K':10, 'A':11}
        if self.name == 'Dealer' and dealer_start:
            card = self.hand[1]
            return card_values[ card[0]]
        
        for card in self.hand:
            if card[0] == 'A':
                aces += 1
            else:
                total += card_values[ card[0]]

        for i in range(aces):
            if total + 11 > 21:
                total += 1
            else:
                total += 11

        return total



def main():

    game = Blackjack()
    game.makeDeck()

    # print( game.deck)        # remove this line after it prints out correctly
    # print( game.pullCard(), len(game.deck))      # remove this line after it prints out correctly
    name = input('What is your name?: ')
    player = Player(name, 500)
    dealer = Player('Dealer', 500)
    playing = True
    wager = 0

    while( playing):
        clear()

        print('You have ${}.'.format(player.getCurrency()))
        while wager == 0 or player.getCurrency() - wager < 0:
            # handle getting and converting wager
            try:
                wager = int(input('How much would you like to wage? '))

                # if wager is too much print message
                if player.getCurrency() - wager < 0:
                    print("Sorry you don't have that much money. Try again!")
            except:
                print('something went wrong, please try again!')

        # print(player.name, dealer.name)        # remove after working correctly
        for i in range(2):
            player.addCard( game.pullCard())
            dealer.addCard( game.pullCard())

        # print( 'Player Hand: {} \nDealer Hand: {}'.format(player.hand, dealer.hand))    # remove after
        player.showHand()
        dealer.showHand()

        player_bust = False         # variable to keep track of player going over 21
        while input('\nWould you like to stay or hit?: ').lower() != 'stay':
            clear()
            # pull card and put into player's hand
            player.addCard( game.pullCard())
            
            # show boyh hands using method
            player.showHand()
            dealer.showHand()

            # check if over 21
            if player.calcHand() > 21:
                player_bust = True      # player busted, keep track for later
                # print('\nYou lose!')       # remove after running correctly
                break                   # break out of the player's loop
            
        # handling the dealer's turn, only run if player didn't bust
        dealer_bust = False
        if not player_bust:
            while dealer.calcHand(False) < 17:      # pass False to calculate all cards

                # pull card and put into dealer's hand
                dealer.addCard( game.pullCard())
                # check if over 21
                if dealer.calcHand(False) > 21:     # pass False to calculate all cards
                    dealer_bust = True
                    # print('You Win')                # remove after running correctly
                    break       # break out of the dealer's loop
                
        clear()
        # show both hands using method
        player.showHand()
        dealer.showHand(False)      # pass False to calculate and show all cards, even when there are 2

        # calculate a winner
        if player_bust:
            print('\nYou busted, better luck next time')
            player.setCurrency(wager, False)
            dealer.setCurrency(wager, True)
        elif dealer_bust:
            print('\nThe dealer busted, you win!')
            player.setCurrency(wager, True)
            dealer.setCurrency(wager, False)
        elif dealer.calcHand(False) > player.calcHand():
            print('\nDealer has higher cards, you lose!')
            player.setCurrency(wager, False)
            dealer.setCurrency(wager, True)
        elif dealer.calcHand(False) < player.calcHand():
            print('\nYou beat the dealer! Congrats')
            player.setCurrency(wager, True)
            dealer.setCurrency(wager, False)
        else:
            print('\nYou pushed, no one wins!')
            
        print('\nYou ended with ${}.'.format( player.getCurrency()))

        print("-" * 30 + "\nType 'quit' to stop playing...")
        ans = input('Would you like to play again? ').lower()

        if ans == 'quit':
            playing = False
        else:
            game.makeDeck()
            player = Player(name, player.getCurrency())
            dealer = Player('Dealer', dealer.getCurrency())

    print('\nThanks for playing!')    


if __name__ == '__main__':
    main()


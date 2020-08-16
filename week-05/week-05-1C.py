# Friday: Creating a shopping cart

from os import system
clear = lambda: system('clear')

clear()     # use it to cleat the terminal output

# global list variable
cart = []

# create function to add items to cart
def addItem(item):
    clear ()
    cart.append(item)
    print('{} has been added.'.format(item))

# create function to remove items from cart
def removeItem(item):
    clear()
    try:
        if item.isdigit():
            item_removed = cart.pop(int(item) - 1)
            print('{} has been removed.'.format(item_removed))
        else:
            cart.remove(item)
            print('{} has been removed.'.format(item))
    except:
        print('Sorry, we could not remove that item.')

# create a function to show items in cart
def showCart():
    clear()
    if cart:
        print('Here is your cart:')
        for i in range(len(cart)):
            print('{}) {}'.format(i + 1, cart[i]))
    else:
        print('Your cart is empty.')


# create function to clear items from cart
def clearCart():
    clear()
    cart.clear()
    print('Your cart is empty.')

# create main function that loops until the user quits
def main():
    done = False
    while not done:
        ans = input('show/add/remove/clear/quit: ').lower()
        # base case
        if ans == 'quit':
            print('Thanks for using our program.')
            x = input('Press any key to exit: ')
            showCart()
            done = True
        elif ans == 'add':
            item = input('What would you like to add? ').title()
            addItem(item)
        elif ans == 'remove':
            showCart()
            item = input('What item would you like to remove? ').title()
            removeItem(item)
        elif ans == 'show':
            showCart()
        elif ans == 'clear':
            clearCart()
        else:
            print('Sorry, that was not an option')



if __name__ == '__main__':      # run the program
    main()
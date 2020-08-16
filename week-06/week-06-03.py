# Wednesday: Tuples, Sets, and Frozensets

from os import system
clear = lambda: system('clear')

clear()     # use it to clean the terminal output

# declaring a tuple
t1 = ('hello', 2, 'hello')      # with parens
t2 = True, 1                    # without parens
print( type(t1), type(t2))      # both are tuples
try:
    t1[0] = 1       # will crash, tuples are immutable once declared
except:
    print('tuples are immutable once declared')

# declaring a set (unique variables)
s1 = set( [1, 2, 3, 1])     # uses the set keyword and square brackets
s2 = {4, 4, 5}              # uses curly brackets, like dictionary
print( type(s1), type(s2))
s1.add(5)       # using the add method to add new items to a set
s1.remove(1)    # using the remove method to get rid of the value 1
print(s1)       # notice when printend it removed the second '1' at the end    
print(s2)

# declaring a frozenset
fset = frozenset( [1, 2, 3, 4])
print( type(fset))

# Wednesday Exercises

# User input
done = False
accounts_list = []
account = input('Please enter a bank account: ').lower()
while not done:
    try:
        accounts_list.append(int(account))
    except:
        print('{} is not a number account'.format(account))

    account = input("Write down other number account or 'exit' to finish: ").lower()
    if account == 'exit':
        exit_pr = True

accounts_list = frozenset(accounts_list)
for account_i in account_list:
    print('Account Number: {}'.format(account_i))

# Converstion
nums = [3, 4, 3, 7, 10]
nums = set(nums)
print(nums)
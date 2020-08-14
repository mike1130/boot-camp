# Thursday: Working with lists

# checking the number of items within a list
nums = [5, 10, 15]
length = len(nums)      # len() returns an integer
print(length)

# accessing specific items of a list with slices
print( nums[ 1 : 3])     # will output items in index 1 and 2
print( nums[ : 2])       # will output items in index 0 and 1
print( nums[ : : 2])     # will print every other index - 0, 2, 4, etc.
print( nums[ -2 : ])     # will output the las two items in list

# adding an item to the back of a list using append
nums = [10, 20]
nums.append(5)
print(nums)             # outputs [10, 20, 5]

# adding a value to the beginning of the list
words = ['ball', 'base']
words.insert(0, 'glove') # first number is the index, second is the value
print(words)

# using pop to remove items and saving to a variable to use later
items = [5, 'ball', True]
items.pop()                 # by default removes the last item
removed_item = items.pop(0) # removes 5 and saves it into the variable
print(removed_item, '\n', items)

# using the remove method with a try and except
sports = ['baseball','soccer','football','hockey']
try:
    sports.remove('soccer')
except:
    print('That item does not exist in the list')
print(sports)

# using min, max, and sum
nums = [5, 3, 9]
print( min(nums))       # will find the lowest number in the list
print( max(nums))       # will find the highest number in the list
print( sum(nums))       # will add all numbers in the list and return the sum

# using sorted on lists for numerical and alphabetical data
nums = [5, 8, 0, 2]
sorted_nums = sorted(nums)      # save to a new variable to use later
print(nums, sorted_nums)        # the original list is intact


# sorting a list with .sort() in-place
nums = [5, 0, 8, 3]
nums.sort()             # alters the original variable directly

# using conditional statements on a list
names = ['Jack', 'Robert', 'Mary']
if 'Mary' in names:
    print('found')      # will run since Mary is in the list
if 'Jimmy' not in names:
    print('not found')  # will run since Jimmy is not in the list

# using conditionals to see if a list is empty
nums = []
if not nums:        # could also say 'if nums == []'
    print('empty')

# using a for loop to print all items in a list
sports = ['baseball','soccer','football','hockey']
for sport in sports:
    print(sport)

# using the while loop to remove a certain value
names = ['Bob', 'Jack', 'Rob', 'Bob', 'Robert']
while 'Bob' in names:
    names.remove('Bob')     # removes all instaces of 'Bob'
print(names)

# Thrusday Exercises

# Rremove Duplicates
names = ['Bob', 'Kenny', 'Amanda', 'Bob', 'Kenny']
for name in names:
    while names.count(name) > 1:
        names.remove(name)
print(names)

# User input
condition = False
words = []
while not condition:
    x = input('Write quit to exit: ').lower()
    if x == 'quit':
        condition = True
        words.append(x)
    else:
        words.append(x)
print(words)


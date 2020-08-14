# Tuesday: For Loops
# for       num             in          range(5)    :
# keyword   temp Variable   keyword     function    ending colon

# writing your first for loop using range
for num in range(5):
    print('Value: {}'.format(num))

# providing the start, stop, and step for the range function
for num in range(2, 10, 2):
    print('Value: {}'.format(num))      # will print all evens between 2 an 10

# printing all characters in a name using the 'in' keyword
name = 'John Smith'
for letter in name:
    print('Value: {}'.format(letter))

# using the continue statement within a foor loop
for num in range(5):
    if num == 3:
        continue
    
    print(num)

# breaking out of a loop using the 'break' keyword
for num in range(5):
    if num == 3:
        break
    
    print(num)

# setting a placeholder using the 'pass' keyword
for i in range(5):
    # TODO: add code to print number
    pass


# Tuesday Exercises

#Divisible by Three
for i in range(1, 101):
    if i % 3 != 0:
        continue

    print('Value: {}'.format(i))

# Only Vowels
vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Write a word: ').lower()
x= []
for letter in word:
    for i in vowels:
        if i == letter:
            x.append(i)
            break

print('{} -> {}'.format(word, x))


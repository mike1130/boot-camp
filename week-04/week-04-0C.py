# Weekly Challenge

# Pyramids
try:
    high = int(input('Enter the high of your pyramid: '))
    for i in range(high):
        print(' ' * (high - i) + ' x' * i)

except:
    print('That is not a valid number')
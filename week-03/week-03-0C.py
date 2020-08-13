# Text-Based RPG

# as it's open-ended this is a sample

print('1: Pick the lock')
print('2: Go to sleep')
ans = input('You awake in a jail cell, what would you like to do?: ')

if ans == '1':
    print('1: Run')
    print('2: Fight')
    ans = input('The door opens, a uard notices you though, what do you do?: ')

    if ans == '1':
        print('You got away, congrats you are free!')
    elif ans == '2':
        print('The guard caught you... you lost!')
    
elif ans == '2':
    print('1: Pick the lock')
    print('2: Go to sleep')
    ans = input('You awake in a jail cell, what would you like to do?: ')

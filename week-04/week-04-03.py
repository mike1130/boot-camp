# Wednesday: While loops

# writing your first while loop
health = 10
while health > 0:
    print(health)
    health -= 1     #forgetting this line will result in infinite loop

# using two or more loops togetjer is called a nested loop
for i in range(2):      # outside loop
    for j in range(3):  # inside loop
        print(i, j)

# Wednesdat Exercises

# User input
condition = False
while not condition:
    x = input('Write quit to exit: ').lower()
    if x == 'quit':
        condition = True

# Double Loop
game_over = False
while not game_over:   
    for i in range(6):
        if i == 3:
            game_over = True
            break
        print(i)


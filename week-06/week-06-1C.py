# Weekly Challenge

# Favorite Food
from os import system
clear = lambda: system('clear')
clear()         # use it to cleant the terminal output

import csv

def creatingCSV():
    with open('favFood.csv', mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Favorite Food?', '# of Votes'])


def saveFood():
    ans = input('What is your favorite food? ')

    with open('favFood.csv', mode='a', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([ans])

    print('Food added!')


def countFood():
    food_count = {}

    with open('favFood.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=';')

        for row in reader:
            if row[0].lower() in food_count:
                food_count[row[0].lower()] += 1
            else:
                food_count[row[0].lower()] = 1

    return food_count


def main():
    # creatingCSV()
    while input('Whould you like to add more? [Y/N] ').lower() != 'n':
        saveFood()

    clear()
    print('Here are the results so far...')

    food_count = countFood()
    for key, value in food_count.items():
        print('{}: {}'.format(key, value))

if __name__ == '__main__':
    main()
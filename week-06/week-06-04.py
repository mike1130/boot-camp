# Thursday: Reading and Writing Files

from os import system
clear = lambda: system('clear')

clear()     # use it to clean the terminal output

# opening/creating and writng to a text file
f = open('test.txt', 'w+')      # open file in writing and reading mode
f.write('this is a test')
f.close()
# appending a file
f = open('test.txt','a')
f.write('\nOh my God!')
f.close()
# reading from a text file
f = open('test.txt','r')
data = f.read()
f.close()
print(data)

# opening/creating and writing to a csv file
import csv
with open('test.csv', mode='w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow( ['name', 'city'])
    writer.writerow( ['Craig Lou', 'Taiwan'])

# reading from csv files
with open('test.csv', mode='r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)

# 'r' It opens the file for reading only
# 'w' Opens file for writing. If file doesn't exist, it creates one
# 'x' Creates a new file. If file exist, the operation fails
# 'a' Open in append mode.  If file doesn't exist, it creates one
# 'b' Open in binary mode
# '+' Will open a file for reading and writing. Good for updating

# Thursday Exercises

# User input
number = input('What is your favorite number?: ')
f = open('fNumber.txt', 'w+')
f.write('Favorite number is {}'.format(number))
f.close()
# 3 doritos después
f = open('fnumber.txt', 'r')
data = f.read()
f.close()
print(data)

# Data Dumping
import csv
data = {
    'name': ['Dave', 'Dennis', 'Peter', 'Jess'],
    'language': ['Python', 'C', 'Java', 'Python']
}
with open('langPrg.csv', mode='w', newline='') as f:
    writer = csv.writer(f, delimiter = ';')
    writer.writerow( data.keys())

    for i in range(len(data['name'])):
        writer.writerow( [data['name'][i], data['language'][i]])

with open('langPrg.csv', mode='r') as f:
    reader = csv.reader(f, delimiter = ';')
    for row in reader:
        print(row)
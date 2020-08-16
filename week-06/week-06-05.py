# Driday: Creating a User Database with CSV Files

from os import system
clear = lambda: system('clear')

clear()         # use it to clean the terminal output

# import all necessary packages to be used
import csv

# creating users.csv
def usersCreating():
    with open('users.csv', mode='x', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['email', 'password'])


# changing password
def changePassword(email):
    password = input('Please, confirm your actual password: ')
    clear()

    emails =[]
    passwords = []
    found = False

    with open('users.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row == [email, password]:
                found = True
            elif row:
                emails.append(row[0])
                passwords.append(row[0])

    if found:
        new_pass = input('Enter your new password')

        emails.append(email)
        passwords.append(new_pass)
        
        with open('users.csv', mode='w') as f:
            writer = csv.writer(f, delimiter=';')

            for i in range(len(emails)):
                writer.writerow( [emails[i], passwords[i]])
    else:
        print('Sorry, those credentials were incorrect')



# handle user registration and writing to csv
def registerUser():
    with open('users.csv', mode='a', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        print('To register, pleas enter your info:')
        email = input('e-mail: ')
        password = input('password: ')
        password2 = input('Re-type password: ')
        clear()
        if password == password2:
            writer.writerow( [email, password])
            print('You are now registered!')
        else:
            print('Something went wrong. Try again.')


# ask for user info and return true to login or false if incorrect info
def loginUser():
    print('To login, please enter your info:')
    email = input('e-mail: ')
    password = input('Password: ')
    clear()
    with open('users.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row == [email, password]:
                print('You are now logged in')
                return True
    print('Something went wrong, try again.')
    return False, email


# main loop
def main(active, logged_in):
    while active:
        if logged_in:
            print('1. Logout\n2. Quit\n3. Change Password')
        else:
            print('1. Login\n2. Register\n3. Quit')

        choice = input('What would you like to do? ').lower()
        clear()
        if choice == 'register' and not logged_in:
            registerUser()
        elif choice == 'login' and not logged_in:
            logged_in, email = loginUser()
        elif choice == 'quit':
            active = False
            print('Thanks for using our software!')
        elif choice == 'logout' and logged_in:
            logged_in = False
            print('You are now logged out.')
        elif choice =='change passsword' and logged_in:
            changePassword(email)
            print('You have changed your password')
        elif choice == 'mike':
            usersCreating()
        else:
            print('Sorry, please try again.')


if __name__ == '__main__':
    # varialbes for main loop
    active = True
    logged_in = False
    main(active, logged_in)
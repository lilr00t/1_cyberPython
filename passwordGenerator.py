import random

# Program header for a password generator
print('Welcome to the password generator')

# Variable to store characters to be used at random for generator
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?0123456789'

# Number variable to ask user for input on how many passwords needed
number = int(input('Amount of passwords to generate: '))

# Length input to ask user how long password needs to be
length = int(input('Your password length: '))

# Prints out passwords
print('\nHere are your passwords: ')

# For loop to take passwords in range of number allocate to passwords, for c in range length take
# passwords += random to chose the password
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
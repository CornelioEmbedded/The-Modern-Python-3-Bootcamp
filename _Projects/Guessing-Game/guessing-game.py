# You have to guess the number that this programm generates randomly

# Import random library
import random

# Generate one random number
num = random.randint(1,10)

# Getting a number from the user
selection = int(input('Type a number from 1 to 10: '))

# Making loop for selection
while num != selection:

    print('Wrong number!')
    print(f'Random number: {num}')

    num = random.randint(1,10)

    selection = selection = int(input('Type a number from 1 to 10: '))

print(f'Random number: {num}')
print('You guess it!')
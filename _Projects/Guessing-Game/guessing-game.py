# You have to guess the number that this programm generates randomly

# Import random library
import random

# Generate one random number
num = random.randint(1,10)

tries = 1
num_tries = 5

# Getting a number from the user
selection = int(input('\nType a number from 1 to 10: '))

# Making loop for selection

while num != selection:

    print('Wrong number!')
    print(f'Random number: {num}')

    tries += 1

    num = random.randint(1,10)

    selection = selection = int(input('Type a number from 1 to 10: '))

print(f'Random number: {num}')
print('\nYou guess it!')
print(f'\nNumber of tries: {tries}')

if tries > num_tries :
    print('You are an idiot :D')
else:
    print('You are smart :)')
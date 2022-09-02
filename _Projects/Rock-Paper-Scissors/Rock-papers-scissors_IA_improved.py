## In this code you play against the computer ROCK PAPER SCISSORS!!!

## Import library
from random import randint   

player_wins = 0
computer_wins = 0


## Initialize a random integer from 0 to 2


times = int(input('How many times do you want to play?: '))

while computer_wins < times and player_wins < times:

    print(f'\nPlayer Score: {player_wins}  Computer Score: {computer_wins}')
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    ## You inputs your choice 
    player = input('\nWrite your choice: ').lower()
    
    rand = randint(0,2)
    
    if rand == 0:
        computer = 'rock'
    elif rand == 1:
        computer = 'scissors'
    else:
        computer = 'paper'

    print(f'Computer choice: {computer}')

    ##Decide who wins
    if player == computer:
        print('\nIts a tie!')

    elif player == 'rock' or player == 'scissors' or player == 'paper':
        if computer == 'rock':
            if player == 'scissors':
                print('\nComputer wins!')
                computer_wins += 1

            elif player == 'paper':
                print('\nYou wins!')
                player_wins += 1

        elif computer == 'paper':
            if player == 'scissors':
                print('\nYou wins!')
                player_wins += 1

            elif player == 'rock':
                print('\nComputer wins!')
                computer_wins += 1

        elif computer == 'scissors':
            if player == 'rock':
                print('\nYou wins!')
                player_wins += 1

            elif player == 'paper':
                print('\nComputer wins!')
                computer_wins += 1

    else:
        print('\nSomething went wrong')
    
if computer_wins > player_wins:
    print('\nYou lost against the computer!')
    
elif player_wins == computer_wins:
    print('\nIt is a tie!')

else:
    print('\nYou win over the computer!!!!')

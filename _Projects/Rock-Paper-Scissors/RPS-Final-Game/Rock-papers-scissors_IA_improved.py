## In this code you play against the computer ROCK PAPER SCISSORS!!!

## Import library
from functions import score,generate_random,decision

player_wins = 0
computer_wins = 0


## Initialize a random integer from 0 to 2


times = int(input('How many times do you want to play?: '))

while computer_wins < times and player_wins < times:

    score(player_wins, computer_wins)

    ## You inputs your choice 

    player = input('\nWrite your choice: ').lower()

    computer = generate_random()

    print(f'Computer choice: {computer}')

    ##Decide who wins
    
    decision(player, computer, computer_wins, player_wins)
    
if computer_wins > player_wins:
    print('\nYou lost against the computer!')
    
elif player_wins == computer_wins:
    print('\nIt is a tie!')

else:
    print('\nYou win over the computer!!!!')

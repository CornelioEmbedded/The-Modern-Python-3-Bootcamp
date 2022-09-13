from random import randint

def score (player_wins, computer_wins):

    print(f'\nPlayer Score: {player_wins}  Computer Score: {computer_wins}')
    print("...rock...")
    print("...paper...")
    print("...scissors...")

def generate_random():

    rand = randint(0,2)

    if rand == 0:
        return 'rock'
    elif rand == 1:
        return 'scissors'
    else:
        return 'paper'

def decision(player, computer, computer_wins,player_wins):

    if player == computer:
        print('\nIts a tie!')

    elif player == 'rock' or player == 'scissors' or player == 'paper':
        if computer == 'rock':
            if player == 'scissors':
                player_wins += 1
                return print('Computer wins')

            elif player == 'paper':
                player_wins += 1
                return print('You wins')
                

        elif computer == 'paper':
            if player == 'scissors':
                player_wins += 1
                return print('You wins')
                

            elif player == 'rock':
                computer_wins += 1
                return print('Computer wins')
                

        elif computer == 'scissors':
            if player == 'rock':
                player_wins += 1
                return print('You wins')
                

            elif player == 'paper':
                computer_wins += 1
                return print('Computer wins')
                
    else:
        return print('Something went wrong')


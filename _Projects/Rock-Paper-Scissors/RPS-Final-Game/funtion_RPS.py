from random import randint

def RPS_Game(times):
    
    computer_wins = 0
    player_wins = 0

    while computer_wins < times and player_wins < times:

        Score_Board(computer_wins, player_wins)

        player_choice = input('\nWrite your choice:')
        computer_choice = Computer_Choice()

        print(f'\nYour choice: {player_choice}')
        print(f'Computer choice: {computer_choice}')

        computer_wins, player_wins = player_vs_computer(player_choice, 
                                computer_choice, computer_wins, player_wins)

def Score_Board(computer, player):

    print(f'\nPlayer Score: {player}  Computer Score: {computer}')
    print("...rock...")
    print("...paper...")
    print("...scissors...")


def Computer_Choice():
    
    rand = randint(0,2)
    
    if rand == 0:
        return'rock'
    elif rand == 1:
        return 'scissors'
    else:
        return 'paper'

def player_vs_computer(player, computer, computer_wins, player_wins):


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

    return computer_wins, player_wins


def Who_Wins(computer, player):
    
    if computer > player:
        print('\nYou lost against the computer!')
    
    elif player == computer:
        print('\nIt is a tie!')

    else:
        print('\nYou win over the computer!!!!')
###
###
###

print('Chose one option: ')
print('... Rock...')
print('...Paper...')
print('...Scissors...')

choice1 = input(' Enter Player 1 choice: ')
choice2 = input(' Enter Player 2 choice: ')

if choice1 != choice2:
    if choice1 ==  'rock':
        if choice2 == 'paper':
            print('player 2 wins!')
        elif choice2 == 'scissors':
            print('player 1 wins!')
    elif choice1 == 'paper':
        if choice2 == 'rock':
            print('player 1 wins!')
        elif choice2 == 'scissors':
            print('player 2 wins!')
    elif choice1 == 'scissors':
        if choice2 == 'rock':
            print('player 2 wins!')
        elif choice2 == 'paper':
            print('player 1 wins!')
else:
    print('Its a tie')
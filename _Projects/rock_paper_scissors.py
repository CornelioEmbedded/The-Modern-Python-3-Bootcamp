###
###
###

print('Chose one option: ')
print('... Rock...')
print('...Paper...')
print('...Scissors...')

choice1 = input(' Enter Player 1´s choice: ')
choice2 = input(' Enter Player 2´s choice: ')

if choice1 == 'paper' and choice2 == 'rock':
    print('Player 1 wins!')
elif choice1 == 'rock' and choice2 == 'scissors':
    print('Player 1 wins!')
elif choice1 == 'scissors' and choice2 == 'paper':
    print('Player 1 wins!')
if choice2 == 'paper' and choice1 == 'rock':
    print('Player 2 wins!')
elif choice2 == 'rock' and choice1 == 'scissors':
    print('Player 2 wins!')
elif choice2 == 'scissors' and choice1 == 'paper':
    print('Player 2 wins!')
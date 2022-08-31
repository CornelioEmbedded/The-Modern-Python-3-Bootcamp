## In this code you play against the computer ROCK PAPER SCISSORS!!!

## Import library
from random import randint   

## You inputs your choice 
player = input('Write your choice: ').lower()

## Initialize a random integer from 0 to 2
rand = randint(0,2)

## Select a number for one of each computer choice
if rand == 0:
    computer = 'rock'
elif rand == 1:
    computer = 'scissors'
else:
    computer = 'paper'

## Print computer choice
print('Computer choice: ' + computer)

##Decide who wins
if player == computer:
    print('Its a tie!')
elif player == 'rock' or player == 'scissors' or player == 'paper':
    if computer == 'rock':
        if player == 'scissors':
            print('Computer wins!')
        elif player == 'paper':
            print('You wins!')
    elif computer == 'paper':
        if player == 'scissors':
            print('You wins!')
        elif player == 'rock':
            print('Computer wins!')
    elif computer == 'scissors':
        if player == 'rock':
            print('You wins!')
        elif player == 'paper':
            print('Computer wins!')
else:
    print('Something went wrong')

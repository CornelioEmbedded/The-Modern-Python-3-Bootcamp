from random import random

def flip_coin():

    ## generate random number
    num = random()

    if num > 0.5:
        return 'Heads'
    else:
        return 'Tails'

print(flip_coin())
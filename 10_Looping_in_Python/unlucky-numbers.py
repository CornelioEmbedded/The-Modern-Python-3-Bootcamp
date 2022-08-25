
## number 4 and 13 are unlucky
## show odd and even numbers

for n in range(1,21):
    if n == 4 or n == 13:
        print(f'{n} is unlucky')
    elif n % 2 != 0:
        print(f'{n} is an odd number')
    else:
        print(f'{n} is an even number')
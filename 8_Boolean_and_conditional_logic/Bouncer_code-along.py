##  ask for age

## age between 18 -21

##if you are +21 = drink 

age = (input('How old are you: '))
if age != "":
    if int(age) <= 18 and int(age) > 21:
        print('You can enter, but not drink')
    elif int(age) >= 21:
        print('You can drink')
    else:
        print('You cant come ine')
else:
    print('You have not enter an age')
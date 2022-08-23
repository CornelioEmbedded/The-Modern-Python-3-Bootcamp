##  AND
##  OR
##  NOT

age = int (input('Enter your age: '))

if age > 2 and age < 4:
    print('Your age is between 2 and 4')
else:
    print('Your number is different!')

city = input('where do you live: ')

if city == 'san francisco' or city == 'los angeles':
    print('You live in california')
else:
    print('You live somewhere else')

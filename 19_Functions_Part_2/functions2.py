
def sum_all_num(*args):
    total = 0

    for n in args:
        total += n
    return total

def name (**kwargs):

    for person, animal in kwargs.items():
        print(f'{person}´s favorite animal is {animal}')


animals = name(cornelio = 'tiger', oksana = 'horse', leo = 'lion')

print(animals)
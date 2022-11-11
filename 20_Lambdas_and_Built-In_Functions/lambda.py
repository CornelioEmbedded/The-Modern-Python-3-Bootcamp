## lambda

# hola = lambda num: num **3

# print(hola(3))

## map

# num = [2,4,6,8,10]

# doubles = map(lambda x: x * 2 , num)

# for num in doubles:
#     print(num),

## all

# people = ['Charlie', 'Casey', 'Cody', 'Cornelio']
# print(all([name[0] == 'C' for name in people]))



def sum_even_values(*args):
    
    lista_suma = []
    for i in args:
        if (i % 2 == 0):
            lista_suma.append(i)
        else:
            print(0)

sum_even_values(1,2,3,4)
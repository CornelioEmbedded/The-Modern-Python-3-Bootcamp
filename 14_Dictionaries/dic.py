instructor = {

    'name' : 'Colt',
    'dogs' : 3,
    'last_name' : 'Posadas',
    'hola': True

}


"METHODS"
## values - give us the value of the key
## keys - give us the key
## items - access all keys and values
## clear - clear all dictionary
## copy - makes a copy of dictionary
## fromkeys - {}.fromkeys - creates key-value from separated values
## get - get the value from the key the corresponding value
## pop - remove an item from the dictionary
## popitem - removes something random from dictionary
## update - take a list and add something a second list

a = {'hola':1, 'adios':2}

a.update(instructor)

print(a)
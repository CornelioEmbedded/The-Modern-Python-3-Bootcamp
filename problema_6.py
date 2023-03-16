
cadena = str(input('Digite cadena:'))

print(f'Longuitud de la cadena de caracteres: {len(cadena)}')

list_cadena = cadena.split(' ')
nueva_cadena = []
count = 0
for item in list_cadena:
    if len(item) == 4:
        count += 1
        nueva_cadena.append(item.replace(item, '****'))
    else:
        nueva_cadena.append(item)

print(f'Hay {count} palabras de cuatro letras')
print(f"Nueva cadena: {' '.join(nueva_cadena)}")
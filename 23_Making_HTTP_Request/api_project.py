import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = colored(figlet_format('DAD JOKE 3000'), color='blue')
print(header)
term = input('What would you like to search?: ')
url = 'https://icanhazdadjoke.com/search?t'
res = requests.get(url, 
                   headers={'Accept': 'application/json'}, 
                   params={'term':term}
                   ).json()
num_jokes = res['total_jokes']
results = res['results']

if num_jokes > 1:
    print(f'I found {num_jokes} jokes about {term}. Here is one:')
    print(choice(results)['joke'])
elif num_jokes == 1:
    print(f'I found one joke about {term}')
    print(results[0]['joke'])
else:
    print('There are no jokes')

import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    URL = '/page/1'
    all_quotes = []
    while URL:
        response = requests.get(f'{BASE_URL}{URL}')
        response_text = response.text.encode('utf8').decode('ascii', 'ignore')
        soup = BeautifulSoup(response_text, features="html5lib")

        quotes = soup.find_all(class_='quote')

        for quote in quotes:
            all_quotes.append({
                'text': quote.find(class_='text').get_text(),
                'author': quote.find(class_='author').get_text(),
                'bio_link': quote.find('a')['href']})

        button = soup.find(class_='next')
        URL = button.find('a')['href'] if button else None
    return all_quotes


def start_game (all_quotes):
    choice_quote = choice(all_quotes)
    remaining_guesses = 4
    print('Here is a quote: ')
    print(choice_quote['text'])
    print(choice_quote['author'])
    guess = ''

    while guess.lower() != choice_quote['author'].lower() and remaining_guesses > 0:
        guess = input(f'Who said this quote? Guesses remaining :{remaining_guesses}\n')
        if guess.lower() == choice_quote['author'].lower():
            print('YOU ARE RIGHT')
            break
        remaining_guesses -= 1

        if remaining_guesses == 3:
            response = requests.get(f"{BASE_URL}{choice_quote['bio_link']}")
            response_text = response.text.encode('utf8').decode('ascii', 'ignore')
            soup = BeautifulSoup(response_text, features="html5lib")
            birth_day = soup.find(class_='author-born-date').get_text()
            birth_place = soup.find(class_='author-born-location').get_text()
            print(f'Here is a hint: The author was born on {birth_day} {birth_place}')

        elif remaining_guesses == 2:
            print(f"Here is a hint: The author's first name starts with: {choice_quote['author'][0]}")

        elif remaining_guesses == 1:
            last_name = choice_quote['author'].split(' ')[1][0]
            print(f"Here is a hint: The author's last name starts with: {last_name}")
        else:
            print(f"No more guesses. The answer was {choice_quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input('Would you like to play again (y/n)?')

    if again.lower() in ('yes', 'y'):
        print('OK, PLAYING AGAIN')
        return start_game(all_quotes)
    else:
        print('BYE!!!!')


def write_quotes(quotes):
    with open('quotes.csv', 'w') as file:
        headers = ['text', 'author', 'bio_link']
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


quotes = scrape_quotes()
write_quotes(quotes)
start_game(quotes)

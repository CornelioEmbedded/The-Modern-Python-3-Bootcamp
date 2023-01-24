import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.rithmschool.com/')

with open('blog_data.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['title', 'link', 'date'])

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        title = article.find('a').get_text()
        url = article.find('a')['href']
        date = article.find('time')['datetime']
        csv_writer.writerow([title, url, date])

# 32 - Web Scraping with BeautifulSoup

## Introduction to Web Scraping
- Web scraping involves programmatically grabbing data from a web page
- Three steps: Download, extract data, use data

### Why Scrape?
- There is data on a site that you want to store or analyze
- You cant get by other means
- You want to programmatically grab the data (instead of lots of manual copying/pasting)

### Is it ok??
- Some websites dont want people scraping them
- Best practice: consult the robots.txt file
- If making many requests, time them out
- If you are too aggressive, your IP can be blocked

## Introduction to Beautiful Soup
- Extract data from HTML
- Beautiful SOup lets us navigate through HTML with Python
- It doesnt download HTML, we need the `requests` module

## Parsing and Navigating HTML
- BeautifulSoup(html_string, "html.parser") - parse HTML
- Once parsed, there are several ways to navigate:
  - By Tag Name
  - Using find - returns one matching tag
  - Using find_all - returns a list of matching tags

```python
from bs4 import BeautifulSoup

soup = BeatifulSoup(html, "html.parser")
d = soup.find()
```

## Navigating with CSS Selectors
- `select`- returns a list of elements matching a CSS selector
  - Selector Cheatsheet
    - Select by id of foo: #foo
    - Select by class of bar: .bar
    - Select children: div > p
    - Select descendents: div p


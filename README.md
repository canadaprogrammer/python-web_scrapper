# Python

## Install Python

1. Download python, https://www.python.org/downloads/

2. Add path

   1. Environment variables

   2. Edit Path on System variables

   3. Add the path:

      - C:\Users\jinpa\AppData\Local\Programs\Python\Python310

      - C:\Users\jinpa\AppData\Local\Programs\Python\Python310\Scripts

3. Check the version

   - python -V

## Install Packages

- Request: HTTP for Humans

  - Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic

  - python -m pip install requests

- beautifulsoup4

  - Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

  - python -m pip install beautifulsoup4

## Scrap All Data form URL

- ```python
  import requests

  costco_results = requests.get('https://www.indeed.com/jobs?q=python&limit=50', timeout=30)

  print(costco_results.text)
  ```

## Pull data out of HTML

- ```python
  import requests
  from bs4 import BeautifulSoup

  indeed_results = requests.get('https://www.indeed.com/jobs?q=python&limit=50', timeout=30)

  indeed_soup = BeautifulSoup(indeed_results.text, 'html.parser')

  pagination = indeed_soup.find('div', {'class': 'pagination'})

  pages = pagination.find_all('a')

  spans = []

  for page in pages:
    spans.append(page.find('span'))

  # exclude the last one
  print(spans[:-1])
  ```

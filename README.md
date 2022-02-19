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

  indeed_results = requests.get('https://www.indeed.com/jobs?q=python&limit=50', timeout=30)

  print(indeed_results.text)
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

## Get the last page number

- The first page of Indeed is showing only five pages on the pagination

  - To get the last page number is `start=99999` on the URL

  - ```python
    indeed_results = requests.get('https://www.indeed.com/jobs?q=python&limit=50&start=99999', timeout=30)

    ...

    for link in links[1:]:
      # pages.append(link.find('span').string)
      pages.append(int(link.string))

    max_page = pages[-1]
    ```

## Request Each Page

- Create `indeed.py`

  - ```python
    import requests
    from bs4 import BeautifulSoup

    LIMIT = 50
    URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

    def extract_indeed_pages():
      results = requests.get(URL + '&start=99999', timeout=30)
      soup = BeautifulSoup(results.text, 'html.parser')
      pagination = soup.find('div', {'class': 'pagination'})

      links = pagination.find_all('a')
      pages = []
      for link in links[1:]:
        # pages.append(link.find('span').string)
        pages.append(int(link.string))

      max_page = pages[-1]
      return max_page

    def extract_indeed_jobs(last_page):
      for page in range(last_page):
        results = requests.get(URL + f'&start={page * LIMIT}', timeout=30)
        print(results.status_code)
    ```

- `main.py`

  - ```python
    from indeed import extract_indeed_pages, extract_indeed_jobs

    last_indeed_page = extract_indeed_pages()

    jobs = extract_indeed_jobs(last_indeed_page)
    ```

## Extract Titles

- On `indeed.py`

  - ```python
    def extract_indeed_jobs(last_page):
      jobs = []
      for page in range(last_page):
        html = requests.get(f'{URL}&start={page * LIMIT}', timeout=30)
        soup = BeautifulSoup(html.text, 'html.parser')
        results = soup.find_all('a', {'class': 'resultWithShelf'})
        for result in results:
          span = result.find('h2', {'class': 'jobTitle'}).find_all('span')
          for s in span:
            if s.get('title') is None:
              continue
            jobs.append(s.get('title'))
      return jobs
    ```

## Extract Companies

- On `indeed.py`

  - ```python
    ...
    for result in results:
      span = result.find('h2', {'class': 'jobTitle'}).find_all('span')
      for s in span:
        if s.get('title') is None:
          continue
        title = s.get('title')
      # strip(): remove spaces from the front and back like trim()
      company = (result.find('span', {'class': 'companyName'}).string).strip()
      print(f'Title: {title},\nCompany Name: {company.strip()}')
    ```

## Encapsulate Extract Job

- On `indeed.py`

  - ```python
    def extract_job(result):
      span = result.find('h2', {'class': 'jobTitle'}).find_all('span')
      for s in span:
        if s.get('title') is None:
          continue
        title = s.get('title')
      company = (result.find('span', {'class': 'companyName'}).string).strip()
      return {'title': title, 'company': company}

    def extract_indeed_jobs(last_page):
      jobs = []
      for page in range(1):
        print(f'Scrapping page {page + 1}')
        html = requests.get(f'{INDEED_URL}&start={page * LIMIT}', timeout=30)
        soup = BeautifulSoup(html.text, 'html.parser')
        results = soup.find_all('a', {'class': 'resultWithShelf'})
        for result in results:
          job = extract_job(result)
          jobs.append(job)
      return jobs
    ```

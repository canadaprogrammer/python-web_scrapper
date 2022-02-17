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
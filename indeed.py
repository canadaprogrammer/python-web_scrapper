import requests
from bs4 import BeautifulSoup

LIMIT = 5
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
  jobs = []
  for page in range(1):
    html = requests.get(f'{URL}&start={page * LIMIT}', timeout=30)
    soup = BeautifulSoup(html.text, 'html.parser')
    results = soup.find_all('a', {'class': 'resultWithShelf'})
    for result in results:
      span = result.find('h2', {'class': 'jobTitle'}).find_all('span')
      for s in span:
        if s.get('title') is None:
          continue
        title = s.get('title')
      # strip(): remove spaces from the front and back like trim()
      company = (result.find('span', {'class': 'companyName'}).string).strip()
      print(f'Title: {title},\nCompany Name: {company}')
  return jobs
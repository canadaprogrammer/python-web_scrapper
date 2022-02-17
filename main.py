import requests
from bs4 import BeautifulSoup

indeed_results = requests.get('https://www.indeed.com/jobs?q=python&limit=50&start=99999', timeout=30)

indeed_soup = BeautifulSoup(indeed_results.text, 'html.parser')

pagination = indeed_soup.find('div', {'class': 'pagination'})

links = pagination.find_all('a')

pages = []

for link in links[1:]:
  # pages.append(link.find('span').string)
  pages.append(int(link.string))

max_page = pages[-1]

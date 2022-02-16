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
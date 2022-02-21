import requests
from bs4 import BeautifulSoup

LIMIT = 3
INDEED_URL = f"https://ca.indeed.com/jobs?q=web%20developer&l=Victoria%2C%20BC&limit={LIMIT}"

def get_last_page():
  results = requests.get(INDEED_URL + '&start=99999', timeout=30)
  soup = BeautifulSoup(results.text, 'html.parser')
  pagination = soup.find('div', {'class': 'pagination'})

  links = pagination.find_all('a')
  pages = []
  for link in links[1:]:
    # pages.append(link.find('span').string)
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page

def get_job(result):
  span = result.find('h2', {'class': 'jobTitle'}).find_all('span')
  for s in span:
    if s.get('title') is None:
      continue
    title = s.get('title')
  # strip(): remove spaces from the front and back like trim()
  company = (result.find('span', {'class': 'companyName'}).string).strip()
  location = result.find('div', {'class': 'companyLocation'}).text
  job_key = result.get('data-jk')
  return {'title': title, 'company': company, 'location': location, 'link': f'https://ca.indeed.com/viewjob?jk={job_key}'}

def get_jobs(last_page):
  jobs = []
  for page in range(1):
    print(f'Scrapping page {page + 1}')
    html = requests.get(f'{INDEED_URL}&start={page * LIMIT}', timeout=30)
    soup = BeautifulSoup(html.text, 'html.parser')
    results = soup.find_all('a', {'class': 'resultWithShelf'})
    for result in results:
      job = get_job(result)
      jobs.append(job)
  return jobs

def get_indeed_jobs():
  last_page = get_last_page()
  jobs = get_jobs(last_page)
  return jobs


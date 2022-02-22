import requests
from bs4 import BeautifulSoup

LINKEDIN_URL = f"https://ca.linkedin.com/jobs/search?keywords=Web%20Developer&location=Victoria%2C%20British%20Columbia%2C%20Canada&distance=100&position=1&pageNum=0"

def get_job(result):
  title = (result.find('h3', {'class': 'base-search-card__title'}).string).strip()
  company = (result.find('a', {'class': 'hidden-nested-link'}).string).strip()
  location = (result.find('span', {'class': 'job-search-card__location'}).string).strip()
  link = result.find('a', {'class': 'base-card__full-link'}).get('href')
  return {'title': title, 'company': company, 'location': location, 'link': link}

def get_jobs():
  jobs = []
  html = requests.get(f'{LINKEDIN_URL}', timeout=30)
  soup = BeautifulSoup(html.text, 'html.parser')
  results = soup.find_all('div', {'class': 'job-search-card'})
  for result in results:
    job = get_job(result)
    jobs.append(job)
  return jobs

def get_linkedin_jobs():
  jobs = get_jobs()
  return jobs


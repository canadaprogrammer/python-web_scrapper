import requests

costco_results = requests.get('https://www.indeed.com/jobs?q=python&limit=50', timeout=30)

print(costco_results.text)
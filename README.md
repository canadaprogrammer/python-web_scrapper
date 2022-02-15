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

  - python -m pip install requests

- beautifulsoup4

  - python -m pip install beautifulsoup4

- ```python
  import requests

  costco_results = requests.get('https://www.indeed.com/jobs?q=python&limit=50', timeout=30)

  print(costco_results.text)
  ```

import requests
from bs4 import BeautifulSoup
import json

URL = 'https://www.monster.com/jobs/search/?q=Software-Engineer&where=Boston&stpage=1&page=10'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

jobs = results.find_all('section', class_='card-content')
job_links = json.loads(BeautifulSoup(page.text, 'html.parser').find_all("script", type="application/ld+json")[1].text)
all_urls = [dct["url"] for dct in job_links["itemListElement"]]

for job, link in zip(jobs, all_urls):
    job_title = job.find('h2', class_='title')
    company = job.find('div', class_='company')
    location = job.find('div', class_='location')
    if None in (job_title, company, location):
        continue
    print(f'Company: \t{company.text.strip()}')
    print(f'Title: \t\t{job_title.text.strip()}')
    print(f'Location: \t{location.text.strip()}')
    print(f'Link: \t\t{link}')
    print()


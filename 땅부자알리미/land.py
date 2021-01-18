import requests
from bs4 import BeautifulSoup

URL = f"https://new.land.naver.com/offices?ms=37.2456145,126.8129905,15&a=TJ&b=A1&e=RETAIL&g=10000&ad=true"

#def get_last_page():
#    result = requests.get(URL)
#    soup = BeautifulSoup(result.text, "html.parser")
#    pages = soup.find("div", {"class": "s-pagination"})#.find_all("a")
#    last_page = pages[-2].get_text(strip=True)
#    return int(last_page)

def extract_info(html):
  result = html.find('div', {'class' : 'item_inner'})
  title = result.find('div',{'class' : 'item_title'}).find("span").string
  print(title)
#  company, location = result.find('h3').find_all('span', recrusive=False)
#  company = company.get_text(strip=True).strip("-")
#  location = location.get_text(strip=True).strip("-")
#  job_id = html['data-jobid']
  return {'title':title, 'company':company, 'location':location, "apply_link" : f"https://stackoverflow.com/jobs/{job_id}"}

#def extract_jobs(last_page):
#  jobs = []
#  for page in range(last_page):
#    print(f"Scrapping SO : page : {page}")
#    result = requests.get(f"{URL}&pg=page{page+1}")
#    soup = BeautifulSoup(result.text, "html.parser")
#    results = soup.find_all("div", {"class":"-job"})
#    for result in results:
#      job = extract_job(result)
#      jobs.append(job)
#    return jobs

#def get_jobs():
#    last_page = get_last_page()
#    jobs = extract_jobs(last_page)
#    return jobs

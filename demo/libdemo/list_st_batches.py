import requests
from bs4 import BeautifulSoup

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
contents = resp.text

soup = BeautifulSoup(contents, 'html.parser')

table = soup.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    title = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text
    print(f"{title:50} {timings:20} {stdate}")

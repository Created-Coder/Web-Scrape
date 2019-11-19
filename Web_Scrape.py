import bs4
import csv
from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import requests

my_url = 'https://www.volunteermatch.org/search/orgs.jsp?l=Ohio&k=&submitsearch=Search'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.find_all("div", {"class":"searchitem"})

filename = "Scraped_data.csv"
f = open(filename, "w")

header = "Organization Name, Mission Statement,Website Link \n"

f.write(header)

for container in containers:
    base_url = "https://www.volunteermatch.org"
    page_url = container.a['href']
    request_href = base_url + page_url
    uClient = uReq(request_href)
    page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")

    Organization_Name = page_soup.find("span", {'class': 'rwd_show'})
    Organization_Name = Organization_Name['title']
    print(Organization_Name)

    Mission_Statement = page_soup.find('div', {'class': 'more_info_col1 left'})
    Mission_Statement = (Mission_Statement.p).get_text()

    Website_Link = page_soup.find('div', {'class': 'more_info_col2 left'})
    Website_Link = Website_Link.a['href']

    f.write(Organization_Name + Mission_Statement + Website_Link + '\n')

for i in range(11, 4191, 10):
    my_url = ('https://www.volunteermatch.org/search/orgs.jsp?aff=&r=region&l=Ohio%2C+USA&o=update&s={}'.format(i))
    uClient = uReq(my_url)
    page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("div", {"class": "searchitem"})
    for container in containers:
        base_url = "https://www.volunteermatch.org"
        page_url = container.a['href']
        request_href = base_url + page_url
        uClient = uReq(request_href)
        page_html = uClient.read()
        page_soup = soup(page_html, "html.parser")

        Organization_Name = page_soup.find("span", {'class': 'rwd_show'})
        Organization_Name = Organization_Name['title']
        print(Organization_Name)


        Mission_Statement = page_soup.find('div', {'class': 'more_info_col1 left'})
        Mission_Statement = (Mission_Statement.p).get_text()

        Website_Link = page_soup.find('div', {'class': 'more_info_col2 left'})
        Website_Link = Website_Link.a['href']

        f.write(Organization_Name + Mission_Statement + Website_Link + '\n')








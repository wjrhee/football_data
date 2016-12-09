import bs4
import requests
from lxml import html

page = "http://www.pro-football-reference.com/years/2016/passing.htm"
htmlPage = requests.get(page)
# tree = html.fromstring(htmlPage.content)
soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
qbTags = soup.tbody.contents
allTds = soup.find_all('td')

for i in allTds:
    if(hasattr(i, 'data-stat')):
        print(i['data-stat'])
        print(i.string)

# def scraping(arr):
#     for item in arr:
#         if(type(item) is bs4.element.Tag and len(item.contents) > 0):
#             scraping(item.contents)
#         elif(item.name == 'td'):
#             print(item)
        # if(type(item) is bs4.element.Tag and len(item.contents) > 0):
        #     scraping(item.contents)
        # else:
        #     print(item)

# scraping(qbTags)

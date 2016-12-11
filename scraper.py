import bs4
import requests

def getHeaders(page):
    headers = []
    headersDescription = []
    htmlPage = requests.get(page)
    soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
    headerSoup = soup.tr
    for item in headerSoup:
        if(hasattr(item, 'data-stat')):
            headers.append(item['data-stat'])
            headersDescription.append(item['aria-label'])
    return {
        'headers': headers,
        'headersDescription': headersDescription
    }

# pass in 'td' for pro-football-reference
def scraping(page, tag):
    htmlPage = requests.get(page)
    soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
    tagSoup = soup.find_all(tag)
    for i in tagSoup:
        if(hasattr(i, 'data-stat')):
            print(i['data-stat'])
            print(i.string)

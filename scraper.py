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
    allData = []
    playerData = []
    htmlPage = requests.get(page)
    soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
    tagSoup = soup.find_all(tag)
    for player in tagSoup:
        for stat in player.contents:
            if(hasattr(stat, 'data-stat')):
                playerData.append(stat.string)
        allData.append(playerData)
        playerData = []
    return allData


    # # TEST ONE DATA SET
    # i = tagSoup[1]
    # for j in i.contents:
    #     print(j)


# testPage = "http://www.pro-football-reference.com/years/2016/passing.htm"
# testTag = 'tr'
# x = scraping(testPage, testTag)
# print(x)
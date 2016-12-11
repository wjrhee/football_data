# TODO - scrape from player pages

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

# pass in 'tr' for pro-football-reference
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

def scrape(page, tag):
    allData = []
    playerData = []
    queue = []
    htmlPage = requests.get(page)
    soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
    tagSoup = soup.find_all(tag)
    for player in tagSoup:
        linkTag = player.a
        if(linkTag is not(None)):
            # link = "http://www.pro-football-reference.com" + str(linkTag['href'])
            # htmlPage = requests.get(link)
            # newSoup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
            # print(newSoup)
            for stat in player.contents:
                if (hasattr(stat, 'data-stat')):
                    playerData.append(stat.string)
            allData.append(playerData)
        playerData = []
    return allData

scrape("http://www.pro-football-reference.com/years/2016/passing.htm", 'tr')
    # # TEST ONE DATA SET
    # i = tagSoup[1]
    # for j in i.contents:
    #     print(j)
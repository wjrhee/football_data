import bs4
import requests
import re
from selenium import webdriver
import os

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
# based on http://www.pro-football-reference.com/years/2016/passing.htm
def scraping(page, tag):
    allData = []
    playerData = []
    htmlPage = requests.get(page)
    soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
    tagSoup = soup.find_all(tag)
    for player in tagSoup:
        linkTag = player.a
        if (linkTag is not (None)):
            for stat in player.contents:
                if(hasattr(stat, 'data-stat')):
                    playerData.append(stat.string)
            allData.append(playerData)
        playerData = []
    return allData

def linkScrape(pageList, linkPattern, tag, excludePattern):
    linksArr = []

    for pageObj in pageList:
        page = pageObj['link']

        htmlPage = requests.get(page)
        soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
        tagSoup = soup.find_all(tag)

        for i in tagSoup:
            if(i.get("href") is not(None)):
                if(re.match(linkPattern, str(i['href'])) is not(None) and excludePattern not in str(i['href'])):
                    link = "http://www.pro-football-reference.com" + str(i['href'])
                    if not any(item['link'] == link for item in linksArr):
                    # if(not(link in linksArr)):
                        print(link)
                        linksArr.append({
                            'name': i.string,
                            'link': link
                        })
    return linksArr


def playerDataScrape(link):
    chromedriver = "/usr/lib/chromium-browser/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(link)

    html = driver.page_source

    soup = bs4.BeautifulSoup(html, "html.parser")

    allTables = soup.find_all("tr")
    coolData = []
    for i in allTables:
        for j in i.contents:
            if(isinstance(j, bs4.element.Tag)):

                if(j.get('data-stat') is not None):
                    # print(j)
                    coolData.append({
                        'title': j['data-stat'],
                        'data': j.string
                    })

    for item in coolData:
        print(item)



def scrape(page):
    teamLinkRegexPattern = r"^/teams/[a-zA-Z]"
    playerLinkRegexPattern = r"^/players/[a-zA-Z]{1}/[a-zA-Z]"
    # allTeamLinksArr = []
    allPlayerLinksArr = []
    allTeamLinksArr = linkScrape([{'link': page}], teamLinkRegexPattern, 'a', 'fantasy')
    allPlayerLinksArr = linkScrape(allTeamLinksArr, playerLinkRegexPattern, 'a', 'fantasy')
    # for teamLink in allTeamLinksArr:

    print(allPlayerLinksArr)
    # for playerLink in allPlayerLinksArr:
        # playerDataScrape(playerLink)


testPage = "http://www.pro-football-reference.com/years/2016/"
page2 = "http://www.pro-football-reference.com/teams/atl/2016.htm"
playerTestPage = "http://www.pro-football-reference.com/players/B/BradTo00.htm"
playerDataScrape(playerTestPage)
# scrape(page2)

# scrape("http://www.pro-football-reference.com/years/2016/passing.htm", 'tr')
    # # TEST ONE DATA SET
    # i = tagSoup[1]
    # for j in i.contents:
    #     print(j)
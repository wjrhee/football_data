# TODO - why can't i get all the tables from the players page?

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

def linkScrape(page, regexPattern, tag):

    linksArr = []
    htmlPage = requests.get(page)
    soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
    tagSoup = soup.find_all(tag)

    for i in tagSoup:
        # print(i.get("href"))
        if(i.get("href") is not(None)):
            if(re.match(regexPattern, str(i['href'])) is not(None)):
                link = "http://www.pro-football-reference.com" + str(i['href'])
                if(not(link in linksArr)):
                    linksArr.append(link)
    return linksArr

def playerDataScrape(link):
    # htmlPage = requests.get(link)
    # soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
    # all_tables = soup.findAll('div', {'class': 'table_wrapper'})
    # test = soup.findAll('table')
    chromedriver = "/usr/lib/chromium-browser/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    driver.get(link)

    html = driver.page_source

    soup = bs4.BeautifulSoup(html, "html.parser")

    allTables = soup.find_all("table")
    print(len(allTables))

    # for tag in soup.find_all('table'):
    #     print(len(tag))

    # print(soup)
    # all = ['passing_playoffs', 'passing', 'passing_advanced']

    # print(all_tables[0].findAll('table'))
    # for i in all_tables:
    #     for j in i.contents:
    #         if(type(j) is bs4.element.Tag):
    #             for k in j.contents:
    #                 print(k)
            # for k in j.contents:
            #     print(k.name)
        # print(i.contents)
        # print(i.table)



def scrape(page):
    teamLinkRegexPattern = r"^/teams/[a-zA-Z]"
    playerLinkRegexPattern = r"^/players/[a-zA-Z]{1}/[a-zA-Z]"
    allTeamLinksArr = []
    allPlayerLinksArr = []
    allTeamLinksArr += linkScrape(page, teamLinkRegexPattern, 'a')
    allPlayerLinksArr += linkScrape(page, playerLinkRegexPattern, 'a')
    for teamLink in allTeamLinksArr:
        allPlayerLinksArr += linkScrape(teamLink, playerLinkRegexPattern, 'a')
    print(allPlayerLinksArr)


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
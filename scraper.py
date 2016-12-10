import bs4
import requests

headers = []
headersDescription = []

page = "http://www.pro-football-reference.com/years/2016/passing.htm"
htmlPage = requests.get(page)
soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')

def getHeaders(soupObj):
    headerSoup = soupObj.tr
    for item in headerSoup:
        if(hasattr(item, 'data-stat')):
            headers.append(item['data-stat'])
            headersDescription.append(item['aria-label'])
            # print(item['data-stat'])
    # print(headers)
    # print(headersDescription)
    return {
        'headers': headers,
        'headersDescription': headersDescription
    }


def scraping(soupObj, tag):
    tagSoup = soupObj.find_all(tag)
    for i in tagSoup:
        if(hasattr(i, 'data-stat')):
            print(i['data-stat'])
            print(i.string)
# scraping(soup, 'td')
k = getHeaders(soup)
# print(k['headers'])


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

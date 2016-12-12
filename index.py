# TODO - scrape for every player
# start at http://www.pro-football-reference.com/years/2016/
# gather team links -> gather player links -> gather player data

import scraper
import db

def main():
    # gathering data for quarterbacks

    page = "http://www.pro-football-reference.com/years/2016/passing.htm"
    page = "http://www.pro-football-reference.com/years/2016/"

    # db.generateTables('quarterbacks', page)
    # allData = scraper.scraping(page, 'tr')
    # headers = scraper.getHeaders(page)
    # db.insertData('quarterbacks', allData, headers['headers'])


if __name__ == "__main__":
    main()

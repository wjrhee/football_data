import scraper
import db

def main():
    # gathering data for quarterbacks
    customQBDataTypesArr = ['varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'integer', 'integer', 'varchar', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer']
    page = "http://www.pro-football-reference.com/years/2016/passing.htm"
    db.generateTables('quarterbacks', customQBDataTypesArr, page)
    allData = scraper.scraping(page, 'tr')
    headers = scraper.getHeaders(page)
    db.insertData('quarterbacks', allData, headers['headers'])


if __name__ == "__main__":
    main()

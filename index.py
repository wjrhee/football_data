import scraper
import db

def main():
    # gathering data for quarterbacks
    customQBDataTypesArr = ['integer', 'varchar', 'varchar', 'integer', 'varchar', 'integer', 'integer', 'varchar', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer']
    page = "http://www.pro-football-reference.com/years/2016/passing.htm"
    db.generateTables('quarterbacks', customQBDataTypesArr, page)
    scraper.scraping(page, 'td')


if __name__ == "__main__":
    main()

import psycopg2
import scraper

# print(scraper.getHeaders(scraper.soup))

headers, headersDescription = [], []
customQBDataTypesArr = ['varchar', 'varchar', 'varchar', 'integer', 'varchar']

def generateTables(tableName):
    checkSQLcommand = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{0}'"
    headerSQLcommand = "CREATE TABLE {0}(id serial PRIMARY KEY,"
    count = 0
    headers = scraper.getHeaders(scraper.soup)
    print(headers['headers'])

    for header in headers['headers']:
        # print(header)
        if (count < len(customQBDataTypesArr)):
            db_dataType = customQBDataTypesArr[count]
        else:
            db_dataType = 'integer'
        if (count == len(headers['headers']) - 1):
            headerSQLcommand = headerSQLcommand + header + " {0}".format(db_dataType)
        else:
            headerSQLcommand = headerSQLcommand + header + " {0}, ".format(db_dataType)
        count += 1

    headerSQLcommand = headerSQLcommand + ");"
    conn = psycopg2.connect("dbname=football user=rheewalt")
    cur = conn.cursor()
    cur.execute(checkSQLcommand.format(tableName))
    if(bool(cur.rowcount)):
        cur.execute("DROP TABLE {0}".format(tableName))
    cur.execute(headerSQLcommand.format(tableName))
    conn.commit()
    cur.close()
    conn.close()

generateTables("aaa")
# print(headerSQLcommand[630:])
# x = [m.start() for m in re.finditer('ranker',headerSQLcommand)]
# print(x)
# print(headerSQLcommand.find('varchar'))
# headerSQLcommand = headers.headers



# cur.execute("SELECT * FROM ")
# print("{0} files copied from {1} into {2}".format(len(final_list), src_path[:len(src_path)-6], dest_path))

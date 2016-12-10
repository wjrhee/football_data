# TODO - making requests in both modules.  Reorganize.

import psycopg2
import bs4
import requests

headers, headersDescription = [], []
page = "http://www.pro-football-reference.com/years/2016/passing.htm"
htmlPage = requests.get(page)
soup = bs4.BeautifulSoup(htmlPage.content, 'html.parser')
customQBDataTypesArr = ['varchar', 'varchar', 'varchar', 'integer', 'varchar']

def generateTables(tableName):
    checkSQLcommand = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{0}'"
    headerSQLcommand = "CREATE TABLE {0}(id serial PRIMARY KEY,"
    count = 0
    headers = getHeaders(soup)
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

generateTables("quaterbacks")
# print(headerSQLcommand[630:])
# x = [m.start() for m in re.finditer('ranker',headerSQLcommand)]
# print(x)
# print(headerSQLcommand.find('varchar'))
# headerSQLcommand = headers.headers



# cur.execute("SELECT * FROM ")
# print("{0} files copied from {1} into {2}".format(len(final_list), src_path[:len(src_path)-6], dest_path))

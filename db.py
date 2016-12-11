# TODO - finish insert data into database function

import psycopg2
import scraper

headers, headersDescription = [], []
customQBDataTypesArr = ['varchar', 'varchar', 'varchar', 'integer', 'varchar']

def generateTables(tableName, db_dataTypeArr, page):
    checkSQLcommand = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{0}'"
    headerSQLcommand = "CREATE TABLE {0}(id serial PRIMARY KEY,"
    count = 0
    headers = scraper.getHeaders(page)

    for header in headers['headers']:
        if (count == len(headers['headers']) - 1):
            headerSQLcommand = headerSQLcommand + header + " {0}".format(db_dataTypeArr[count])
        else:
            headerSQLcommand = headerSQLcommand + header + " {0}, ".format(db_dataTypeArr[count])
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

def insertData(data):
    insertSQLcommand = ""
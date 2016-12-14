import psycopg2
import scraper

headers, headersDescription = [], []

def generateTables(tableName, page):
    checkSQLcommand = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{0}'"
    headerSQLcommand = "CREATE TABLE {0}(id serial PRIMARY KEY,"
    count = 0
    headers = scraper.getHeaders(page)

    for header in headers['headers']:

        if (count == len(headers['headers']) - 1):
            headerSQLcommand = headerSQLcommand + header + " varchar"
            # headerSQLcommand = headerSQLcommand + header + " {0}".format(db_dataTypeArr[count])
        else:
            headerSQLcommand = headerSQLcommand + header + " varchar, "
            # headerSQLcommand = headerSQLcommand + header + " {0}, ".format(db_dataTypeArr[count])
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

def insertData(tableName, dataObj, headers):

    conn = psycopg2.connect("dbname=football user=rheewalt")
    insertSQLcommand = "INSERT INTO {0} (".format(tableName)

    insertObj = dataObj[1:]

    for player in insertObj:
        count = 0

        for header in headers:
            insertSQLcommand = insertSQLcommand + header
            if (count != len(headers) - 1):
                insertSQLcommand += ', '
            count += 1

        insertSQLcommand += ") VALUES ("
        count = 0

        for data in player:
            cleanData = apostropheReplacer(str(data))
            insertSQLcommand += "'{0}'".format(cleanData)
            if(count != len(player) - 1):
                insertSQLcommand += ", "
            count += 1
        count = 0
        insertSQLcommand += ")"

        cur = conn.cursor()
        cur.execute(insertSQLcommand)
        conn.commit()
        cur.close()
        print(insertSQLcommand)
        insertSQLcommand = "INSERT INTO {0} (".format(tableName)
    conn.close()


def apostropheReplacer(str):
    # For cases like Le'Veon Bell, the apostrophe needs to be replaced with two
    str = str.replace('\'', '\'\'')
    return str
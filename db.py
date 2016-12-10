import psycopg2
conn = psycopg2.connect("dbname=football user=rheewalt")
cur = conn.cursor()
cur.execute("SELECT * FROM ")

import psycopg2

db = psycopg2.connect("dbname=news")

cursor = db.cursor()

cursor.execute( "select from authors where")

results = cursor.fetchall()

print results

db.close()



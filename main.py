# Reference from https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
import psycopg2

query1 = "select title, count(*) from log join articles on log.path like concat('%', articles.slug, '%') where status = '200 OK' group by title order by count desc;"
query2 = "select name, count(*) from articles join authors on authors.id = articles.author join log on log.path like concat('%', articles.slug, '%') where log.status = '200 OK' group by authors.name order by count desc;"
query3 = ""

try:
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()

    # 1. What are the most popular three articles of all time?
    cur.execute(query2)
    rows = cur.fetchall()
    for row in rows:
        print(str(row[0]) + ' , ' + str(row[1]) + ' views')

    # 2. Who are the most popular article authors of all time?
    # cur.execute("select name, count(name) from authors right join articles on authors.id = articles.author group by name order by count desc;")

except:
    print "I am unable to connect to the database"


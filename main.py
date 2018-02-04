# Reference from https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
import psycopg2

query1 = "select title, count(*) from log join articles on log.path like concat('%', articles.slug, '%') where status = '200 OK' group by title order by count desc;"
query2 = "select name, count(*) from articles join authors on authors.id = articles.author join log on log.path like concat('%', articles.slug, '%') where log.status = '200 OK' group by authors.name order by count desc;"
query3 = "select date_trunc('day', time), count (*), (select count(*) from log where status != '200 OK')," \
         "100.0 * count (*) / (select count(*) from log where status != '200 OK') ::float from log where status != '200 OK' group by 1 order by 2 desc;"

try:
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()

    # query 1
    cur.execute(query1)
    rows = cur.fetchall()
    for row in rows:
        print(str(row[0]) + ' , ' + str(row[1]) + ' views')

    print('\n\n\n')

    # query 2
    cur.execute(query2)
    rows = cur.fetchall()
    for row in rows:
        print(str(row[0]) + ' , ' + str(row[1]) + ' views')

    print('\n\n\n')

    # query 1
    cur.execute(query3)
    rows = cur.fetchall()
    for row in rows:
        print(str(row[0]) + ' , ' + str(row[3]) + '% errors')

except Exception as e:
    print "I am unable to connect to the database"
    print e
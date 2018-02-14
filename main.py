#!/usr/bin/env python

# Reference from https://wiki.postgresql.org/wiki/Psycopg2_Tutorial

import psycopg2
from datetime import datetime

query1 = """ SELECT title, count(*) FROM log JOIN articles ON
         log.path = '/article/'||articles.slug
         WHERE status = '200 OK'
         GROUP BY title ORDER BY count DESC LIMIT 3;"""
query2 = """ SELECT name, count(*) FROM articles JOIN authors ON
         authors.id = articles.author JOIN log ON
         log.path = '/article/'||articles.slug
         WHERE log.status = '200 OK'
         GROUP BY authors.name ORDER BY count DESC;"""
query3 = """ SELECT DATE(time) AS date,
        sum(case when status != '200 OK' then 1 else 0 end) AS fail,
        sum(case when status = '200 OK' then 1 else 0 end) AS success
        FROM log GROUP BY date ORDER BY date DESC;"""


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

    # query 3
    cur.execute(query3)
    rows = cur.fetchall()
    for row in rows:
        fail = float(row[1])
        success = float(row[2])
        error = fail/success
        if  error > 0.01:
            print(str(row[0]) + ' , ' + str(error) + '% errors')

except Exception as e:
    print "I am unable to connect to the database"

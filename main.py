#!/usr/bin/env python

# Reference from https://wiki.postgresql.org/wiki/Psycopg2_Tutorial

import psycopg2

query1 = """ SELECT title, count(*) FROM log JOIN articles ON
         log.path = '/article/'||articles.slug
         WHERE status = '200 OK'
         GROUP BY title ORDER BY count DESC LIMIT 3;"""
query2 = """ SELECT name, count(*) FROM articles JOIN authors ON
         authors.id = articles.author JOIN log ON
         log.path = '/article/'||articles.slug
         WHERE log.status = '200 OK'
         GROUP BY authors.name ORDER BY count DESC;"""
query3 = """ SELECT date, 
        round(100.0 * fail / (success+fail), 2) as percen
        FROM (
        SELECT DATE(time) AS date,
        sum(case when status != '200 OK' then 1 else 0 end) AS fail,
        sum(case when status = '200 OK' then 1 else 0 end) AS success
        FROM log GROUP BY date ORDER BY date DESC) AS date_detail
        WHERE 100.0 * fail / (success+fail) > 1 ;"""


try:
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()

    # query 1
    cur.execute(query1)
    rows = cur.fetchall()
    print("\nWhat are the most popular three articles of all time?\n")
    for row in rows:
        print("{}, {} views".format(row[0],row[1]))

    print('\n\n\n')

    # query 2
    cur.execute(query2)
    rows = cur.fetchall()
    print("\nWho are the most popular article authors of all time? \n")
    for row in rows:
        print("{}, {} views".format(row[0],row[1]))

    print('\n\n\n')

    # query 3
    cur.execute(query3)
    rows = cur.fetchall()
    print("\nOn which days did more than 1% of requests lead to errors? \n")
    for row in rows:
        print("{}, {}% erros".format(row[0],row[1]))

except Exception as e:
    print "I am unable to connect to the database"

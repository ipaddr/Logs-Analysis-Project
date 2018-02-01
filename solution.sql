Question 1 : select path, count(*) from log where status = '200 OK' group by path order by count desc;
Question 2 : select name, count(*) from articles join authors on authors.id = articles.author join log on log.path like concat('%', articles.slug, '%') where log.status = '200 OK' group by authors.name order by count desc;
Question 3 :

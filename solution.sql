Question 1 : select title, count(*) from log join articles on log.path like concat('%', articles.slug, '%') where status = '200 OK' group by title order by count desc;
Question 2 : select name, count(*) from articles join authors on authors.id = articles.author join log on log.path like concat('%', articles.slug, '%') where log.status = '200 OK' group by authors.name order by count desc;
Question 3 : SELECT date_trunc('day', time) as “date” , count(*) as 'total' from log where status != '200 OK' group by 1 order by count desc

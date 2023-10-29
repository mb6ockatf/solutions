/*
pgsql
https://www.codewars.com/kata/589cf45835f99b2909000115
*/

SELECT date, count_per_date AS count,
	SUM(count::int)
	OVER (ORDER BY date ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) 
		AS total
FROM (
	SELECT DATE(created_at) AS date, COUNT(*) AS count_per_date, COUNT(1)
	FROM posts
	GROUP BY 1
) AS count_per_date;
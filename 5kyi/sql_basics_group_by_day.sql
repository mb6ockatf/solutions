/*
pgsql
https://www.codewars.com/kata/5811597e9d278beb04000038
*/

SELECT date_trunc('day', events.created_at) AS day, description, count(*)
FROM events
WHERE events.name = 'trained'
GROUP BY day, events.description
ORDER BY day;
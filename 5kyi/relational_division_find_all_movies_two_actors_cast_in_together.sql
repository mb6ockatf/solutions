/*
pgsql
https://www.codewars.com/kata/5817b124e7f4576fd00020a2
*/

SELECT film.title
FROM film
  INNER JOIN film_actor AS film_actor1
  ON film.film_id = film_actor1.film_id
  INNER JOIN film_actor AS film_actor2
  ON film.film_id = film_actor2.film_id
WHERE film_actor1.actor_id = 105
  AND film_actor2.actor_id = 122
ORDER BY 1 ASC;
/*
pgsql
https://www.codewars.com/kata/5818bde9559ff58bd90004a2
*/

WITH the_couple(actor1, actor2, sorter) AS (
	SELECT film_actor2.actor_id AS actor1,
		film_actor1.actor_id AS actor2,
		count(film_actor1.actor_id) AS sorter
	FROM film_actor AS film_actor1, film_actor AS film_actor2
	WHERE film_actor1.actor_id <> film_actor2.actor_id
		AND film_actor1.film_id = film_actor2.film_id
	GROUP BY film_actor2.actor_id, film_actor1.actor_id
	ORDER BY sorter DESC, film_actor2.actor_id
	LIMIT 1
)

SELECT concat(actor1.first_name, ' ', actor1.last_name) AS first_actor,
       concat(actor2.first_name, ' ', actor2.last_name) AS second_actor,
	     film.title
FROM film, the_couple, actor AS actor1, actor AS actor2
WHERE the_couple.actor1 = actor1.actor_id AND
	the_couple.actor2 = actor2.actor_id AND
	film.film_id IN (
		SELECT film_actor1.film_id
		FROM film_actor AS film_actor1, film_actor AS film_actor2
		WHERE film_actor1.film_id = film_actor2.film_id AND
			film_actor1.actor_id = actor1.actor_id AND
			film_actor2.actor_id = actor2.actor_id
	)
	ORDER BY film.title;
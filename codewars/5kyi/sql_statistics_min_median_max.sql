/*
pgsql
https://www.codewars.com/kata/58167fa1f544130dcf000317
*/

SELECT min(result.score) AS MIN,
  PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY result.score) AS MEDIAN,
  max(result.score) AS MAX
FROM result;
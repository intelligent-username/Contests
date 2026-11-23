--      https://leetcode.com/problems/not-boring-movies/description/?envType=study-plan-v2&envId=top-sql-50
--      Not Boring movies
--      COMPLETE

SELECT id, movie, description, rating
FROM Cinema
WHERE id % 2 != 0 AND description NOT LIKE '%boring%'
ORDER BY rating DESC;

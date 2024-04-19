-- https://leetcode.com/problems/big-countries/submissions/1230417431/?envType=study-plan-v2&envId=top-sql-50
-- "Big Countries"
--  COMPLETE

SELECT name, population, area
FROM World
WHERE population >= 25000000 OR area >= 3000000;

-- https://leetcode.com/problems/biggest-single-number/
-- Biggest Single Number
-- COMPLETE

SELECT MAX(num) AS num
FROM (
  SELECT num
  FROM MyNumbers
  GROUP BY num
  HAVING COUNT(*) = 1
) temp;

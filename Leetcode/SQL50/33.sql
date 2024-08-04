-- https://leetcode.com/problems/consecutive-numbers/submissions/1343647182/?envType=study-plan-v2&envId=top-sql-50
-- CONSECUTIVE NUMBERS
-- COMPLETE

SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.num = l2.num AND l1.id = l2.id - 1
JOIN Logs l3 ON l1.num = l3.num AND l1.id = l3.id - 2;
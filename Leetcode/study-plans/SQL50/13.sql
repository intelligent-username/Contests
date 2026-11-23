--         https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=top-sql-50
--         Managers with at least 5 ...
--      COMPLETE

SELECT m.name
FROM Employee e
JOIN Employee m ON e.managerId = m.id
GROUP BY m.id, m.name
HAVING COUNT(e.id) >= 5

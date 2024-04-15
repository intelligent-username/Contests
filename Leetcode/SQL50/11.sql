-- https://leetcode.com/problems/employee-bonus/?envType=study-plan-v2&envId=top-sql-50
-- Employee Bonuses
--      COMPLETE

SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000
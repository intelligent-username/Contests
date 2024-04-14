/* https://leetcode.com/problems/students-and-examinations/?envType=study-plan-v2&envId=top-sql-50
Student and Examinations */

SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000 
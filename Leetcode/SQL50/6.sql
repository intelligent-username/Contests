-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50
-- Replace Employee ID with ID

SELECT CASE WHEN EUNI.unique_id IS NULL THEN NULL ELSE EUNI.unique_id END AS unique_id, E.name
FROM Employees AS E
LEFT JOIN EmployeeUNI AS EUNI ON E.id = EUNI.id;

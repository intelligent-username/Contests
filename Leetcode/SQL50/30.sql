-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50
-- The Number of Employees Which Report to Each Employee

SELECT 
    e.employee_id,
    e.name,
    COUNT(r.employee_id) AS reports_count,
    ROUND(AVG(r.age)) AS average_age
FROM 
    Employees e
JOIN 
    Employees r ON e.employee_id = r.reports_to
GROUP BY 
    e.employee_id, e.name
ORDER BY 
    e.employee_id;

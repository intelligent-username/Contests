--     https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50
--     Project employees I
--     COMPLETE

SELECT Project.project_id, 
       ROUND(AVG(Employee.experience_years), 2) AS average_years
FROM Project
JOIN Employee ON Project.employee_id = Employee.employee_id
GROUP BY Project.project_id;

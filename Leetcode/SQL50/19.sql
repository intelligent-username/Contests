-- https://leetcode.com/problems/queries-quality-and-percentage/submissions/1236927929/?envType=study-plan-v2&envId=top-sql-50
-- BEST QUERIES
-- INCOMPLETE

SELECT query_name, 
    ROUND((SUM(rating/position)/COUNT(query_name)),2) AS quality,            
    ROUND(AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END)*100,2) AS poor_query_percentage 
FROM Queries 
GROUP BY query_name
;

-- FROM https://github.com/Qian-Yu-2020/Leetcode-Problems/blob/master/Others%20/%23%201211.%20Queries%20Quality%20and%20Percentage.sql; TRY TO UNDERSTAND
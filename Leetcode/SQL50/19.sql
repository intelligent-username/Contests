-- https://leetcode.com/problems/queries-quality-and-percentage/submissions/1236927929/?envType=study-plan-v2&envId=top-sql-50
-- BEST QUERIES
-- COMPLETE

SELECT query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(SUM(rating < 3) * 100 / COUNT(*), 2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name;

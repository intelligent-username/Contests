-- https://leetcode.com/problems/product-sales-analysis-iii/
-- Product Sales Analysis III
-- COMPLETE

SELECT 
    s.product_id, 
    MIN(s.year) AS first_year, 
    s.quantity, 
    s.price
FROM 
    Sales s
JOIN 
    (SELECT product_id, MIN(year) AS first_year
     FROM Sales
     GROUP BY product_id) f
ON 
    s.product_id = f.product_id 
AND 
    s.year = f.first_year
GROUP BY 
    s.product_id, s.year, s.quantity, s.price;

-- https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&envId=top-sql-50
-- Recyclable and Low Fat Products
-- COMPLETE

SELECT product_id
FROM products
WHERE low_fats = "Y" 
AND recyclable = "Y"; 

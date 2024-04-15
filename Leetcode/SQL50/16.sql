--      https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50
--      Average Selling Price
--      INCOMPLETE; 15/17 pass

SELECT 
    p.product_id, 
    ROUND(SUM(u.units * p.price) / SUM(u.units), 2) AS average_price
FROM Prices p
JOIN UnitsSold u ON p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;

-- https://leetcode.com/problems/immediate-food-delivery-ii/description/?envType=study-plan-v2&envId=top-sql-50
-- Immediate Food Delivery II
-- COMPLETE

WITH first_orders AS (
    SELECT 
        customer_id, 
        order_date, 
        customer_pref_delivery_date,
        RANK() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM Delivery
)
SELECT 
    ROUND(100.0 * SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(*), 2) AS immediate_percentage
FROM first_orders
WHERE rn = 1;

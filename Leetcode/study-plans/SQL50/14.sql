--                  https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50
--                   Confirmation Rate
--      COMPLETE

SELECT 
    s.user_id,
    IFNULL(ROUND(SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(c.action), 2), 0) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id

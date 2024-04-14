-- https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50

SELECT id
FROM Weather w
WHERE EXISTS (
  SELECT 1
  FROM Weather prev_day
  WHERE prev_day.recordDate = DATE_SUB(w.recordDate, INTERVAL 1 DAY)
    AND prev_day.temperature < w.temperature
);

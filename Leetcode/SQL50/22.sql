-- https://leetcode.com/problems/game-play-analysis-iv/
-- Game Play Analysis 4
-- COMPLETE

WITH first_login AS (
  SELECT player_id, MIN(event_date) AS first_login_date
  FROM Activity
  GROUP BY player_id
)
SELECT ROUND(COUNT(DISTINCT fl.player_id) * 1.0 / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM first_login fl
JOIN Activity a ON fl.player_id = a.player_id AND a.event_date = DATE_ADD(fl.first_login_date, INTERVAL 1 DAY);

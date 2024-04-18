    -- https://leetcode.com/problems/percentage-of-users-attended-a-contest/submissions/1235308094/?envType=study-plan-v2&envId=top-sql-50
    -- Percentage of Users Attending a Contest
    -- COMPLETE

SELECT contest_id, ROUND(COUNT(user_id)*100.00/(SELECT COUNT(*) from users),2) AS percentage
FROM register
GROUP BY contest_id  
ORDER BY percentage DESC, contest_id

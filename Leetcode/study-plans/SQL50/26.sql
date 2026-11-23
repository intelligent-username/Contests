-- https://leetcode.com/problems/classes-more-than-5-students/
--  Classes with more than 5 people
-- COMPLETE

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;

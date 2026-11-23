/* https://leetcode.com/problems/average-time-of-process-per-machine/?envType=study-plan-v2&envId=top-sql-50
Average Processing Time Per Machine */
--      COMPLETE

SELECT
    machine_id,
    ROUND(AVG(end_timestamp - start_timestamp), 3) AS processing_time
FROM
    (SELECT
        machine_id,
        process_id,
        MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_timestamp,
        MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_timestamp
    FROM
        Activity
    GROUP BY
        machine_id, process_id) AS process_times
GROUP BY
    machine_id
ORDER BY
    machine_id; 

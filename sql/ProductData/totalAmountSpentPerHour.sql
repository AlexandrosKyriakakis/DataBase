SELECT
   HOUR(trans_time),
   CAST(SUM(A.total_cost) AS DECIMAL (20 , 2 ))
FROM
   transact A,
   bought B
WHERE
   A.transact_id = B.transact_id
GROUP BY HOUR(trans_time)
ORDER BY SUM(A.total_cost) DESC , HOUR(trans_time)
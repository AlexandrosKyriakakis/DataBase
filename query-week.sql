use AlexJohnChris;
SELECT 
    WEEK(t.trans_date) Week,
    YEAR(t.trans_date) Year,
    AVG(total_cost) WeekAvg
FROM
    bought AS b,
    transact AS t
WHERE
    b.transact_id = t.transact_id
GROUP BY WEEK(t.trans_date) 
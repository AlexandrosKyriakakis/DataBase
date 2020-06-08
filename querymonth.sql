use AlexJohnChris;
SELECT b.card_id, MONTHNAME(t.trans_date), AVG(t.total_cost)
FROM transact as t, bought as b
WHERE b.transact_id = t.transact_id 
GROUP BY b.card_id, MONTHNAME(t.trans_date)
ORDER BY b.card_id, MONTH(t.trans_date);
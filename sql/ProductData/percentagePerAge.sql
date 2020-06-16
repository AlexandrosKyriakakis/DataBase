SELECT distinct
   cast(SUM(
IF(A.age < 20, 1, 0))/totals.total _ 100 as decimal
(20,2)) AS 'Under 20',
   cast
(SUM
(
IF(A.age BETWEEN 20 AND 29, 1, 0))/totals.total _ 100 as decimal
(20,2)) AS '20 - 29',
   cast
(SUM
(
IF(A.age BETWEEN 30 AND 39, 1, 0))/totals.total _ 100 as decimal
(20,2)) AS '30 - 39',
   cast
(SUM
(
IF(A.age BETWEEN 40 AND 49, 1, 0))/totals.total _ 100 as decimal
(20,2)) AS '40 - 49',
   cast
(SUM
(
IF(A.age BETWEEN 50 AND 59, 1, 0))/totals.total _ 100 as decimal
(20,2)) AS '50 - 59',
   cast
(SUM
(
IF(A.age BETWEEN 60 AND 69, 1, 0))/totals.total _ 100 as decimal
(20,2)) AS '60 - 69',
   cast
(SUM
(
IF(A.age >= 70, 1, 0))/totals.total _ 100 as decimal
(20,2)) AS 'Over 70',
   HOUR
(C.trans_time) AS Hour
FROM
(SELECT distinct
   YEAR(CURDATE()) - YEAR(birth_date) -
IF(STR_TO_DATE(CONCAT(YEAR(CURDATE()),
         '-', MONTH(birth_date), '-', DAY(birth_date)), '%Y-%c-%e') > CURDATE(), 1, 0) AS age,
         card_id
   FROM
         customer) A,
(SELECT _
from bought
group by transact_id)
B
LEFT JOIN
   transact C on B.transact_id = C.transact_id,
(SELECT distinct
   COUNT(D.transact_id) as total, HOUR(D.trans_time) as total_hour
FROM
   transact D
GROUP BY HOUR(D.trans_time)
ORDER BY HOUR(D.trans_time)
) totals
WHERE
   A.card_id = B.card_id
   AND B.transact_id = C.transact_id
   AND totals.total_hour = HOUR
(C.trans_time)
GROUP BY HOUR
(C.trans_time)
ORDER BY HOUR
(C.trans_time)
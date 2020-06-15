select A.barcode, B.barcode, count(A.barcode)
from bought A, bought B
where A.transact_id = B.transact_id and A.barcode>B.barcode
group by A.barcode, B.barcode
order by count(A.barcode) desc, A.barcode, B.barcode
limit 100;

select A.store_id, A.shelf, A.alley, count(B.barcode)
from has A, bought B
where A.barcode = B.barcode
group by B.barcode, A.store_id, A.shelf, A.alley
order by count(B.barcode) desc;

select A.category, A.special_note,  count(B.barcode)
from product A, bought B
where A.barcode = B.barcode and A.category = 'Κάβα'
group by A.special_note, A.category
#order by count(B.barcode) desc;

select hour(trans_time), cast(sum(A.total_cost) as decimal(20,2))
from transact A, bought B
where A.transact_id = B.transact_id 
group by hour(trans_time)
order by sum(A.total_cost) desc, hour(trans_time)

SELECT 
SUM(IF(age < 20,1,0)) as 'Under 20',
SUM(IF(age BETWEEN 20 and 29,1,0)) as '20 - 29',
SUM(IF(age BETWEEN 30 and 39,1,0)) as '30 - 39',
SUM(IF(age BETWEEN 40 and 49,1,0)) as '40 - 49',
SUM(IF(age BETWEEN 50 and 59,1,0)) as '50 - 59',
SUM(IF(age BETWEEN 60 and 69,1,0)) as '60 - 69',
SUM(IF(age >= 70 ,1,0)) as 'Over 70', hour(C.trans_time) as Hour
from (select 
YEAR(CURDATE()) - 
YEAR(birth_date) - 
IF(STR_TO_DATE(CONCAT(YEAR(CURDATE()), '-', MONTH(birth_date), '-', DAY(birth_date)) ,'%Y-%c-%e') > CURDATE(), 1, 0) 
AS age, card_id
FROM customer
) A, bought B, transact C
where A.card_id = B.card_id and B.transact_id = C.transact_id
group by hour(C.trans_time)
order by hour(C.trans_time)

g: Να βρούμε τη σχετικη απόδοση κάθε προιοντος ταξινομημένα
δλδ Εγω παίρνω ντομάτες date-Δευτερα και ξαναπαίρνω την date-τεταρτη 
και το κοστος τους εινια 4€ και ο χρονος καταναλωσης είναι 3 μέρες
θέλω ευρω ανα χρονο 4/72 = 0.05 κόστος δια χρόνο ζωης 
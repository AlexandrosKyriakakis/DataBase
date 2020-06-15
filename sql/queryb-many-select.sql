use AlexJohnChris;
set @n=0;
set @k=0;
SELECT 
    a.card_id, a.barcode, a.sum_quantity
FROM
(select @n := @n +1 n,aa.card_id,aa.barcode,aa.sum_quantity 
from (
select card_id,barcode,sum(quantity) as sum_quantity
from bought
group by card_id, barcode
order by card_id, sum(quantity) desc) as aa) as a
WHERE
    (SELECT 
            COUNT(*)
        FROM
            (select @k := @k +1 k,bb.card_id,bb.barcode,bb.sum_quantity 
from (
select card_id,barcode,sum(quantity) as sum_quantity
from bought
group by card_id, barcode
order by card_id, sum(quantity) desc) as bb) as b
        WHERE
            (b.card_id = a.card_id AND b.k >= a.n)) < 11
ORDER BY a.card_id ASC , a.sum_quantity DESC
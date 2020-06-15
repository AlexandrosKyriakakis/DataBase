use John;
SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 1
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 100;

select p.category, h.store_id, count(*)
FROM product p, has h, bought b
WHERE b.store_id = h.store_id
AND p.barcode = h.barcode
AND h.barcode = b.barcode 
AND p.category = 'Φρέσκα Προϊόντα'
GROUP BY h.store_id
order by count(*) desc
LIMIT 10;
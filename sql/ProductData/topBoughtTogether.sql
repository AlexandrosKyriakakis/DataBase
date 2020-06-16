SELECT
   A.barcode, B.barcode, COUNT(A.barcode)
FROM
   bought A,
   bought B
WHERE
   A.transact_id = B.transact_id
   AND A.barcode > B.barcode
GROUP BY A.barcode , B.barcode
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 100;
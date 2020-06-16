SELECT
   A.store_id, A.shelf, A.alley, COUNT(B.barcode)
FROM
   has A,
   bought B
WHERE
   A.barcode = B.barcode
GROUP BY B.barcode , A.store_id , A.shelf , A.alley
ORDER BY COUNT(B.barcode) DESC
LIMIT 100;
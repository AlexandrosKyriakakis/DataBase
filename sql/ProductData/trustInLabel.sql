SELECT
   A.category,
   A.special_note,
   COUNT(B.barcode) / COUNT(C.barcode) * 100 AS percentage
FROM
   product A,
   bought B,
   product C
WHERE
   A.barcode = B.barcode
   AND B.barcode = C.barcode
   AND A.special_note = 1
GROUP BY A.special_note , A.category
ORDER BY percentage DESC;
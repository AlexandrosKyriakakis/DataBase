use John;
SELECT
   A.category,
   A.special_note,
   COUNT(B.barcode) / E.total * 100 AS percentage
FROM
   product A,
   bought B,
   (SELECT COUNT(C.barcode) as total, C.category as categor
   FROM bought C, product D
   WHERE C.barcode = D.barcode
   GROUP BY D.category)E
WHERE
    A.barcode = B.barcode
   and A.category = E.categor
   AND A.special_note = 0
GROUP BY A.special_note , A.category
ORDER BY percentage DESC;
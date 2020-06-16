(SELECT
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
LIMIT 1)
union
(SELECT
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
AND B.store_id = 2
AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT
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
AND B.store_id = 3
AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT
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
AND B.store_id = 4
AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT
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
AND B.store_id = 5
AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT
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
AND B.store_id = 6
AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT
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
AND B.store_id = 7
AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT
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
AND B.store_id = 8
AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT
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
AND B.store_id = 9
AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT
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
AND B.store_id = 10
AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)

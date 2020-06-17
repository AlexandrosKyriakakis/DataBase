# Product Data

## Top Bought together

```sql
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
```

## Top popular positions

```sql
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
```

## Trust in label

```sql
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
```

## Total amount spent per hour per age

```sql
 distinct
   cast(SUM(IF(A.age < 20, 1, 0))/totals.total _ 100 as decimal(20,2)) AS 'Under 20',
   cast(SUM(IF(A.age BETWEEN 20 AND 29, 1, 0))/totals.total _ 100 as decimal(20,2)) AS '20 - 29',
   cast(SUM(IF(A.age BETWEEN 30 AND 39, 1, 0))/totals.total _ 100 as decimal(20,2)) AS '30 - 39',
   cast(SUM(IF(A.age BETWEEN 40 AND 49, 1, 0))/totals.total _ 100 as decimal(20,2)) AS '40 - 49',
   cast(SUM(IF(A.age BETWEEN 50 AND 59, 1, 0))/totals.total _ 100 as decimal(20,2)) AS '50 - 59',
   cast(SUM(IF(A.age BETWEEN 60 AND 69, 1, 0))/totals.total _ 100 as decimal(20,2)) AS '60 - 69',
   cast(SUM(IF(A.age >= 70, 1, 0))/totals.total _ 100 as decimal (20,2)) AS 'Over 70',
   HOUR(C.trans_time) AS Hour
FROM
   (SELECT distinct
         YEAR(CURDATE()) - YEAR(birth_date) - IF(STR_TO_DATE(CONCAT(YEAR(CURDATE()),
         '-', MONTH(birth_date), '-', DAY(birth_date)), '%Y-%c-%e') > CURDATE(), 1, 0) AS age,
         card_id
   FROM
         customer) A,
   (SELECT _ from bought group by transact_id) B
LEFT JOIN
   transact C on B.transact_id = C.transact_id,
   (SELECT distinct
   COUNT(D.transact_id) as total, HOUR(D.trans_time) as total_hour
   FROM
   transact D
   GROUP BY HOUR(D.trans_time)
   ORDER BY HOUR(D.trans_time)) totals
WHERE
   A.card_id = B.card_id
   AND B.transact_id = C.transact_id
   AND totals.total_hour = HOUR(C.trans_time)
GROUP BY HOUR(C.trans_time)
ORDER BY HOUR(C.trans_time)
```

## Personal Query #1

Most Popular Shops per Category.

```sql
(select p.category, h.store*id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store*id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Φρέσκα Προϊόντα'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store*id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Ποϊόντα Ψυγείου'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store*id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Κατοικίδια'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store*id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Κάβα'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store*id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Είδη Σπιτιού'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store_id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Προσωπικής Περιποίησης'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(\*) as counter
FROM product p, has h, bought b
WHERE b.store_id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Είδη Σπιτιού'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
```

## Personal Query #2

Most Popular Paths in each Store.

```sql
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
```

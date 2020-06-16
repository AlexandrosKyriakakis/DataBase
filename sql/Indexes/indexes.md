# Indexes

use AlexJohnChris;
CREATE INDEX hour_trans ON transact(time);
CREATE INDEX special_bit ON product(special_note);
CREATE INDEX category_indx ON product(category);

Considering that MySQL adds indexes on every primary key of our database, we chose to
add the above three additional indexes on columns that are used frequently in our queries to speeden up our database search time.
For example the second index is clearly useful to the query presented below which makes extensive
use of the special note
column:

SELECT
A.category,
A.special_note,
COUNT(B.barcode) / COUNT(C.barcode) \* 100 AS percentage
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

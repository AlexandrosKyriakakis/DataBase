## Views

## Sales per category per store

```sql
SELECT * FROM sales_category_store
```

### Code to create view #1

```sql
use AlexJohnChris;
CREATE VIEW sales_category_store
AS
SELECT B.transact_id, B.card_id, H.barcode, B.quantity, P.category, H.store_id
FROM
bought B, has H, product P
WHERE B.barcode = H.barcode
AND H.barcode = P.barcode
ORDER BY P.category, H.store_id

```

## Customer Info

```sql
SELECT * FROM customer_info
```

### Code to create view #2

```sql
use AlexJohnChris;
CREATE VIEW customer_info
AS
SELECT DISTINCT c.card_id, c.first_name, c.last_name, c.total_points, c.rewards, c.birth_date, c.marital_status, c.social_security_number, c.sex, p.phone_number
FROM
customer c
LEFT JOIN
customer_phone p
on c.card_id = p.card_id
```

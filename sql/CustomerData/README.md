# Customer Data

An example of queries in page `/customers_visit_data` using `card_id = 99`.

## Stores Visited

```sql
SELECT
   distinct b.card_id, b.store_id
FROM
   bought as b, store as s
where
   b.store_id = s.store_id
   AND b.card_id = 99
   order by card_id, store_id
```

## Most Popular Items Bought

```sql
SELECT card_id, barcode, sum(quantity)
FROM bought
where card_id = 99
group by barcode
order by sum(quantity) desc
limit 10
```

## Average total amount spent per month

```sql
SELECT
    b.card_id, MONTHNAME(t.trans_date),
    cast(AVG(t.total_cost) as decimal(6,2))
FROM
    transact AS t,
    bought AS b
WHERE
   b.card_id = 99
   AND b.transact_id = t.transact_id
GROUP BY MONTHNAME(t.trans_date)
ORDER BY MONTH(t.trans_date);
```

## Average total amount spent per week

```sql
SELECT
   b.card_id,
   WEEK(t.trans_date) Week,
   cast(AVG(total_cost) as decimal(6,2))
FROM
   bought AS b,
   transact AS t
WHERE
   b.card_id = 99
   AND b.transact_id = t.transact_id
GROUP BY WEEK(t.trans_date)
```

## Chart

```sql
select hour(trans_time), count(hour(trans_time))
from transact
where transact_id
   in (
	      select transact_id
	      from bought
         where card_id = 99
      )
group by hour(trans_time)
order by hour(trans_time)
```

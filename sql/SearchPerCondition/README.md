# Search Per Condition

Example of an sql Query at the page `/search`

```sql
select
   transact.transact_id,transact.total_cost,
   transact.trans_date,transact.trans_time,
   transact.week_day,transact.payment_method,
   bought.card_id,bought.barcode,bought.quantity
from transact, bought
where
   bought.transact_id = transact.transact_id
   and bought.store_id = 2
   and month(transact.trans_date) = month('1980-11-01')
   and year(transact.trans_date) = year('1980-11-01')
   and bought.quantity >= 4
   and bought.barcode = 5000665
   and transact.total_cost >= 3.0
   and transact.payment_method = 'Card'
   and bought.barcode in (select barcode from product where category = 'Είδη Σπιτιού')
   limit 1000
```

# Edit Data

## Stores

### Add Stores

Adding a Test Store.

```sql
insert into store
   (phone,city,store_address,postal_code,
   opening_time,closing_time ,square_meters)
values
   ('1111111','Test','Test','1111',
   '08:00:00','21:00:00','1111')
```

### Update the Test Store

```sql
update store
set
   phone = '222222' , city = 'NewTest' ,
   store_address = 'NewTest' , postal_code = '22222',
   opening_time = '09:00:00' , closing_time = '22:00:00' ,
   square_meters = '22222'  where store_id = 11;
```

### Remove the Test Store

```sql
DELETE FROM store WHERE store_id = 11
```

## Products and Customers

We follow the same pattern for editing both Products and Customers

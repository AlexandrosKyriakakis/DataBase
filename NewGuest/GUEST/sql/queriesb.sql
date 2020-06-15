set @givenCustomerID = '948';
set @Something = '4000046';
/* 10 Most popular products */

select sum(quantity) 
from bought 
where card_id = @givenCustomerID
and barcode in (select barcode from bought where card_id = @givenCustomerID);

1.
select  barcode,quantity 
from bought 
where card_id = 948 and barcode in (select barcode from bought where card_id = 948 );
2.
select  card_id,sum(quantity) 
from bought 
group by barcode, card_id;
3.
select  card_id, barcode,quantity 
from bought 
where card_id = 788;
4.
select  card_id,sum(quantity) 
from bought 
where card_id = 788
group by barcode;
5.
select  card_id,barcode,sum(quantity) 
from bought 
group by card_id, barcode
order by card_id, sum(quantity) DESC;


|customer | product #1 | .... | product #10

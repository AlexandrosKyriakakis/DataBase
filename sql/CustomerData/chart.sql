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
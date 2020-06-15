/* Ολες που έχουν γινει σε ένα ΣΥΓΚΕΚΡΙΜΕΝΟ ΚΑΤΑΣΤΗΜΑ */
/* Give me the store id */ 
/* Θα έχει μια επιλογή για το αν θελει αν δει και τα προιοντα που αγοράστηκαν ή απλα το τρανσακτιον */
/* Μονο Transactions */
SET @AskedStore = 4;
select * from transact where transact_id in (
    select transact_id from bought where store_id = @AskedStore);
/* Αν θέλουμε να δουμε και τα προιοντα κάνουμε*/
select * from bought where store_id = @AskedStore;
/* Aν τα θελουμε στο ιδιο table  */
select * 
    from bought,transact 
    where bought.store_id = @AskedStore 
    and transact.transact_id 
    in (
        select transact_id from bought where store_id = @AskedStore
        ); /* Everything */

/* Βαση ημερομηνίας*/
SET @AskedStore = 4;
set @AskedDate = '1983-09-18';
select transact.transact_id,transact.total_cost,
		transact.trans_date,transact.trans_time,
        transact.week_day,transact.payment_method,
        bought.card_id,bought.barcode,bought.quantity
	from transact, bought
	where transact.transact_id
	in (
		select transact_id from bought where store_id = @AskedStore
		)
	and transact.trans_date = @AskedDate
	and bought.store_id = @AskedStore /* Εδώ αλλάζει */
	and bought.transact_id = transact.transact_id;

/* Βαση Έτους */
SET @AskedStore = 4;
set @AskedDate = '1983';
select transact.transact_id,transact.total_cost,
		transact.trans_date,transact.trans_time,
        transact.week_day,transact.payment_method,
        bought.card_id,bought.barcode,bought.quantity
	from transact, bought
	where transact.transact_id
	in (
		select transact_id from bought where store_id = @AskedStore
		)
	and bought.store_id = @AskedStore
	and bought.transact_id = transact.transact_id
    and year(transact.trans_date) = @AskedDate; /* Εδώ αλλάζει */
/* Ομοια μπορουμε να το κανουμε με ή/και μηνα-μερα οπως το ετος*/
/* Μονάδες προιοντος*/
/* Αν εννοει απο καποιο απο τα προιοντα*/
SET @AskedStore = 4;
set @AskedQuantity = 5;
select transact.transact_id,transact.total_cost,
		transact.trans_date,transact.trans_time,
        transact.week_day,transact.payment_method,
        bought.card_id,bought.barcode, bought.quantity
	from transact, bought
	where transact.transact_id
	in (
		select transact_id from bought where store_id = @AskedStore
        )
	and bought.store_id = @AskedStore
	and bought.transact_id = transact.transact_id
	and bought.quantity >= @AskedQuantity; /* Εδώ αλλάζει */

/* Αν εννοει απο συγκεκριμένο προιον*/
SET @AskedStore = 4;
set @AskedQuantity = 5;
set @AskedBarcode = '6130157';
select transact.transact_id,transact.total_cost,
		transact.trans_date,transact.trans_time,
        transact.week_day,transact.payment_method,
        bought.card_id,bought.barcode, bought.quantity
	from transact, bought
	where transact.transact_id
	in (
		select transact_id from bought where store_id = @AskedStore
        )
	and bought.store_id = @AskedStore
	and bought.transact_id = transact.transact_id
	and bought.quantity >= @AskedQuantity /* Εδώ αλλάζει */
    and bought.barcode = @AskedBarcode; /* Εδώ αλλάζει */
/* To ποσο της συνολικής αγοράς */
SET @AskedStore = 4;
set @AskedTotal = 5;
select transact.transact_id,transact.total_cost,
		transact.trans_date,transact.trans_time,
        transact.week_day,transact.payment_method,
        bought.card_id,bought.barcode, bought.quantity
	from transact, bought
	where transact.transact_id
	in (
		select transact_id from bought where store_id = @AskedStore
        )
	and bought.store_id = @AskedStore
	and bought.transact_id = transact.transact_id 
	and transact.total_cost >= @AskedTotal;/* Εδώ αλλάζει */
/* Cash or Card */
SET @AskedStore = 4;
set @AskedMethod = 'Card';
select transact.transact_id,transact.total_cost,
		transact.trans_date,transact.trans_time,
        transact.week_day,transact.payment_method,
        bought.card_id,bought.barcode, bought.quantity
	from transact, bought
	where transact.transact_id
	in (
		select transact_id from bought where store_id = @AskedStore
        )
	and bought.store_id = @AskedStore
	and bought.transact_id = transact.transact_id
	and transact.payment_method = @AskedMethod; /* Εδώ αλλάζει */
/* Category */
SET @AskedStore = 4;
set @AskedCategory = 'Κάβα';
select transact.transact_id,transact.total_cost,
		transact.trans_date,transact.trans_time,
        transact.week_day,transact.payment_method,
        bought.card_id,bought.barcode, bought.quantity
	from transact, bought
	where transact.transact_id
	in (
		select transact_id from bought where store_id = @AskedStore
        )
	and bought.store_id = @AskedStore
	and bought.transact_id = transact.transact_id
	and bought.barcode in (select barcode from product where category = @AskedCategory); /* Εδώ αλλάζει */

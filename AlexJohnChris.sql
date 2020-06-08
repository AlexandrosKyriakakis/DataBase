CREATE DATABASE `AlexJohnChris`;
ALTER DATABASE AlexJohnChris CHARACTER SET utf8 COLLATE utf8_bin;
USE `AlexJohnChris`;
/* create table Store*/
CREATE TABLE store(
				store_id TINYINT NOT NULL AUTO_INCREMENT,  
				phone BIGINT,
				city CHAR(100),
				store_address VARCHAR(100) NOT NULL ,
				postal_code INT,
                opening_time TIME,
				closing_time TIME,
				square_meters INT,
				CONSTRAINT PKstore PRIMARY KEY (store_id));

/* create table Customer*/ /* THA XRHSIMOPOIHSOUME SUMBASH 0 _ _ _ _ => customer eswterikou, 1 _ _ _ _ => customer ekswterikou, 3 _ _ _ _ => customer etairia*/
CREATE TABLE customer(
				card_id INT NOT NULL AUTO_INCREMENT,  
				first_name VARCHAR(100) NOT NULL,
				last_name VARCHAR(100) NOT NULL,
				total_points BIGINT DEFAULT 0,
                rewards BIGINT DEFAULT 0,
				birth_date DATE,
				marital_status CHAR(15), 
				social_security_number BIGINT NOT NULL,
				sex CHAR(15),
				CONSTRAINT PKcustomer PRIMARY KEY (card_id));

/*customer_phone multivalued attribute of customer*/
CREATE TABLE customer_phone(
				card_id INT,
                phone_number BIGINT NOT NULL,
                CONSTRAINT PKcustomer_phone PRIMARY KEY(card_id, phone_number),
				CONSTRAINT FKcustomer_phone FOREIGN KEY (card_id) REFERENCES customer(card_id) ON UPDATE CASCADE ON DELETE CASCADE );

/* create table Transaction*/
CREATE TABLE transact(
				transact_id BIGINT NOT NULL AUTO_INCREMENT,
                total_cost FLOAT NOT NULL,
                trans_date DATE NOT NULL,
                trans_time TIME NOT NULL,
                week_day CHAR(15),
                payment_method CHAR(15) NOT NULL,
				CONSTRAINT PKtransact PRIMARY KEY (transact_id));

/* create table Product*/
CREATE TABLE product(
				barcode BIGINT NOT NULL,
				product_name VARCHAR(101) NOT NULL, /* Added name*/
				producer_name VARCHAR(50) NOT NULL, /* Added producer name*/
                price FLOAT NOT NULL,
                special_note BIT(1) NOT NULL, /* To kana bit gt mas niazei mono an anoikei h den anhkei sto katasthma 0 -> gia kseno 1 gia AB*/
                category CHAR(25) NOT NULL,
                CONSTRAINT PKvehicle PRIMARY KEY (barcode));

/* works : 1-n relationship (optional,optional)*/
CREATE TABLE has(
				store_id TINYINT NOT NULL,
                barcode BIGINT NOT NULL,
				shelf INT NOT NULL,
                alley INT NOT NULL,
				CONSTRAINT PKhas PRIMARY KEY (store_id, barcode),
				CONSTRAINT FK1store FOREIGN KEY (store_id) REFERENCES store(store_id) ON UPDATE CASCADE ON DELETE CASCADE,
				CONSTRAINT FK2has_products FOREIGN KEY (barcode) REFERENCES product(barcode) ON UPDATE CASCADE ON DELETE CASCADE);

/*  past_prices 1-n relationship(optional,mandatory)*/
CREATE TABLE past_prices(
				barcode BIGINT NOT NULL,
                past_price FLOAT NOT NULL,
				time_of_change TIMESTAMP NOT NULL, 
				CONSTRAINT PKpast_prices PRIMARY KEY (barcode,time_of_change),/*SOS*/
				CONSTRAINT FKhad_price FOREIGN KEY (barcode) REFERENCES product(barcode) ON UPDATE CASCADE ON DELETE CASCADE );


/*  rents: n-m-k-l relationship(optional,optional,optional,mandatory)   the transaction part is mandatory*/
/* payment transactions*/
CREATE TABLE bought(
				transact_id BIGINT NOT NULL,
				card_id INT NOT NULL,
				barcode BIGINT NOT NULL,
				store_id TINYINT NOT NULL,
				quantity INT NOT NULL,
				CONSTRAINT PKbought PRIMARY KEY (transact_id, card_id, barcode, store_id),
				CONSTRAINT FK1product FOREIGN KEY (barcode) REFERENCES product(barcode) ON UPDATE CASCADE ON DELETE CASCADE,
                CONSTRAINT FK2customer FOREIGN KEY (card_id) REFERENCES customer(card_id) ON UPDATE CASCADE ON DELETE CASCADE,
                CONSTRAINT FK3transact FOREIGN KEY (transact_id) REFERENCES transact(transact_id) ON UPDATE CASCADE ON DELETE CASCADE,
                CONSTRAINT FK4store FOREIGN KEY (store_id) REFERENCES store(store_id) ON UPDATE CASCADE ON DELETE CASCADE);
                
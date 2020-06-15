# Database Project

## Overview
[Serious Company](ec2-3-23-63-204.us-east-2.compute.amazonaws.com:8587/) is a website built from scratch for an academic project on lesson NTUA-DATABASES at Nation Technical University of Athens. The website contains random data simulating market database.

## [Requirements](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/requirements.txt)
- mysql
- flask 1.1.2
- mysql_connector 2.2.9
- numpy 1.17.4
- pandas 0.25.3

## ER-Diagram
 ![](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/img/er-diagram.png)

## Relational Model
![](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/img/Relational_Model.png)

## Instalation 

1. At first, initialize a mysql database at either a [localhost](https://dev.mysql.com/doc/mysql-getting-started/en/) or a [server](https://aws.amazon.com/rds/)
2. Then, run the folowing command in terminal, using your credentials in order to connect in mysql host:
```bash
	  mysql -h "server-name" -u "your_username" -p "your_password"
```
### Run the following inside mysql command prompt
3. [AlexJohnChris.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/AlexJohnChris.sql) to create the database.
4. [indexes.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/indexes.sql) to create the indexes.
5. [view1.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/view1.sql) and [view2.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/view2.sql) to create the views.
6. [past_price_trigger.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/past_price_trigger.sql) to create the trigger for auto-update past prices.
7. [addStores.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/addStores.sql) to add all the stores.
### Back in the terminal
8. Run,
```bash 
	git clone https://github.com/AlexandrosKyriakakis/DataBase.git 
	cd DataBase
	git clone https://github.com/AlexandrosKyriakakis/MarketDataset.git 
```
9. Add your database credentials at the top '\*\*\*\*' of each of the following files,
	- [addCustomersAndPhone.py](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/addData/addCustomersAndPhone.py)
	- [addProductsPastPricesHas.py](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/addData/addProductsPastPricesHas.py)
	- [addTransactionsBought.py](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/addData/addTransactionsBought.py)
	- [server_guest.py](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/server_guest.py)
## Authors
- [Alexandros Kyriakakis](https://github.com/AlexandrosKyriakakis)
- [Ioannis Alexopoulos](https://github.com/galexo)

## Licence
This project uses [MIT license](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/LICENCE)


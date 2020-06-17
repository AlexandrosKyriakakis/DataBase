# Database Project

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![Build Status](https://img.shields.io/badge/mysql-v8.0.19+-red.svg)](https://img.shields.io/badge/mysql_connector-v2.2.9-blue.svg)
![Dependencies](https://img.shields.io/badge/flask-v1.1.2-blue)
[![GitHub Issues](https://img.shields.io/badge/numpy-v1.17.4-green.svg)](https://img.shields.io/badge/pandas-v0.25.3-yellow.svg)
![mysql_connector](https://img.shields.io/badge/mysql_connector-v2.2.9-blue.svg)
[![pandas](https://img.shields.io/badge/pandas-v0.25.3-yellow.svg)](https://opensource.org/licenses/MIT)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

[Serious Company](https://damp-thicket-93938.herokuapp.com/) is a website built from scratch for an academic project on lesson NTUA-DATABASES at Nation Technical University of Athens. The website contains random data simulating market database.

## [Requirements](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/requirements.txt)

- mysql 8.0.19
- flask 1.1.2
- mysql_connector 2.2.9
- numpy 1.17.4
- pandas 0.25.3

## ER-Diagram

![](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/img/er-diagram.png?raw=true)

## Relational Model

![](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/img/relationalModel.png?raw=true)

## Installation

1. At first, initialize a mysql database at either a [localhost](https://dev.mysql.com/doc/mysql-getting-started/en/) or a [server](https://aws.amazon.com/rds/)
2. Then, run the folowing command in terminal, using your credentials in order to connect in mysql host:

```bash
	 $ mysql -h "server-name" -u "your_username" -p "your_password"
```

### Run the following inside mysql command prompt, strictly at this order,

3. [AlexJohnChris.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/AlexJohnChris.sql) to create the database.
4. [indexes.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/Indexes/indexes.sql) to create the indexes.
5. [view1.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/views/view1.sql) and [view2.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/views/view2.sql) to create the views.
6. [past_price_trigger.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/trigers/past_price_trigger.sql) to create the trigger for auto-update past prices.
7. [addStores.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/addStores/addStores.sql) to add all the stores.

### Back in the terminal

8. Run,

```bash
	$ git clone https://github.com/AlexandrosKyriakakis/DataBase.git
	$ cd DataBase
	$ git clone https://github.com/AlexandrosKyriakakis/MarketDataset.git
```

9. Add your database credentials at the top '\*\*\*\*' of each of the following files,
   - [addCustomersAndPhone.py](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/addData/addCustomersAndPhone.py)
   - [addProductsPastPricesHas.py](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/addData/addProductsPastPricesHas.py)
   - [addTransactionsBought.py](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/addData/addTransactionsBought.py)
   - [server_guest.py](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/server_guest.py)
10. Run the following strictly at this order,

```bash
	$ pip3 install -r requirements.txt
	$ python3 ./addData/addCustomersAndPhone.py
	$ python3 ./addData/addProductsPastPricesHas.py
	$ python3 ./addData/addTransactionsBought.py
```

11. Now, that the database is full with random generated data, start the back-end server to finish the installation,

```bash
	$ python3 server_guest.py
```

12. Open your favorite browser and type <http://localhost:8587/> to preview the website.

## Sql Queries

Queries to construct database,

- [AlexJohnChris](https://github.com/AlexandrosKyriakakis/DataBase/tree/master/sql)
- [Indexes](https://github.com/AlexandrosKyriakakis/DataBase/tree/master/sql/Indexes)
- [Trigers](https://github.com/AlexandrosKyriakakis/DataBase/tree/master/sql/trigers)
- [Add Stores](https://github.com/AlexandrosKyriakakis/DataBase/tree/master/sql/addStores)

Here we show all the [queries](https://github.com/AlexandrosKyriakakis/DataBase/tree/master/sql) used in the site at each page,

- [SearchPerCondition](https://github.com/AlexandrosKyriakakis/DataBase/tree/master/sql/SearchPerCondition) for page [/search](https://damp-thicket-93938.herokuapp.com/search)
- [CustomerData](https://github.com/AlexandrosKyriakakis/DataBase/tree/master/sql/CustomerData) for pages [/customers_visit_data](https://damp-thicket-93938.herokuapp.com/customers_visit_data) and [/customers](https://damp-thicket-93938.herokuapp.com/customers)
- [ProductData](https://github.com/AlexandrosKyriakakis/DataBase/tree/master/sql/ProductData) for pages at [Product Data](https://damp-thicket-93938.herokuapp.com)
- [Views](https://github.com/AlexandrosKyriakakis/DataBase/tree/master/sql/views) for pages [/customer_info](https://damp-thicket-93938.herokuapp.com/customer_info) and [/sales_category_store](https://damp-thicket-93938.herokuapp.com/sales_category_store)
- [EditData](https://github.com/AlexandrosKyriakakis/DataBase/tree/master/sql/EditData) for pages at [Edit Data](https://damp-thicket-93938.herokuapp.com)

## Authors

- [Alexandros Kyriakakis](https://github.com/AlexandrosKyriakakis)
- [Ioannis Alexopoulos](https://github.com/galexo)

## Licence

This project uses [MIT license](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/LICENCE)

# Database Project

## Overview
[Serious Company](ec2-3-23-63-204.us-east-2.compute.amazonaws.com:8587/) is a website built from scratch for an academic project on lesson NTUA-DATABASES at Nation Technical University of Athens.

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
2. Then, run the folowing command in the terminal in order to connect in mysql host:
```bash
	  mysql -h "server-name" -u "your_username" -p "your_password"
```
### Inside mysql
3. Run [AlexJohnChris.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/AlexJohnChris.sql) to create the database.
4. Run [indexes.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/indexes.sql) to create the indexes.
5. Run [view1.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/view1.sql) and [view2.sql](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/sql/view2.sql) to create the views.
6.  


## Authors
- [Alexandros Kyriakakis](https://github.com/AlexandrosKyriakakis)
- [Ioannis Alexopoulos](https://github.com/galexo)

## Licence
This project uses [MIT license](https://github.com/AlexandrosKyriakakis/DataBase/blob/master/LICENCE)


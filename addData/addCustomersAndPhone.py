import mysql.connector
import pandas as pd
import numpy as np
People = pd.read_csv("./GitWithMyLove/data/RandomPeople.csv")
mydb = mysql.connector.connect(
    host = "db-ece-ntua.cqkzf2d0epmt.us-east-2.rds.amazonaws.com",
    user = "Alexandros",
    passwd = "el17001el12163",
    database = "Alex"
)

mycursor = mydb.cursor()
rewardAll = np.arange(1,100,1)
pointsAll = np.arange(1,1000,1)
phones = np.arange(2100000000,2109999999,10)
for i in range(len(People)):
#   ssn,first_name,last_name,email,gender,birth
    first_name = People['first_name'][i].replace("'","").replace('"',"")
    last_name = People['last_name'][i].replace("'","").replace('"',"") 
    email = People['email'][i]
    sex = People['gender'][i]
    total_points = np.random.choice(pointsAll)
    rewards = np.random.choice(rewardAll)
    mar = 'Widow' if sex == 'Female' else 'Widower'
    social_security_number = People['ssn'][i].replace('-','')
    birth_date = People['birth'][i]
    marital_status = np.random.choice(['Married','Single','Divorced','Engaged',mar])
    sqlFormula = """INSERT INTO customer (first_name,last_name,birth_date,marital_status,sex,social_security_number,total_points,rewards) 
                    VALUES ('{}','{}','{}','{}','{}',{},{},{})""".format(first_name,last_name,birth_date,marital_status,sex,social_security_number,total_points,rewards)
    mycursor.execute(sqlFormula)
    mydb.commit() #Save Data
    for k in range(3):
        sqlFormula = """INSERT INTO customer_phone (card_id,phone_number)
                        VALUES ({},{})""".format(i+1,np.random.choice(phones))
        mycursor.execute(sqlFormula)
    mydb.commit() #Save Data

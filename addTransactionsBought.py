import mysql.connector
import random as rd
import pandas as pd
import numpy as np
ab = pd.read_csv("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Βάσεις Δεδομένων/GitWithMyLove/data/AB.csv")
mydb = mysql.connector.connect(
    host = "db-ece-ntua.cqkzf2d0epmt.us-east-2.rds.amazonaws.com",
    user = "Alexandros",
    passwd = "el17001el12163",
    database = "AlexJohnChris"
)

mycursor = mydb.cursor()
cardAll = np.arange(1,1000,1)
storeAll = np.arange(1,11,1)
CostAll = np.arange(1,200,0.1)
year,month,day = np.arange(1970,2019,1), np.arange(1,12,1), np.arange(1,29,1)
hour,minute,second = np.arange(10,23,1), np.arange(10,59,1), np.arange(10,59,1)
for i in range(len(ab)):
    total_cost = np.random.choice(CostAll)
    trans_date = "-".join([str(np.random.choice(year)),str(np.random.choice(month)), str(np.random.choice(day))])
    trans_time = ":".join([str(np.random.choice(hour)),str(np.random.choice(minute)), str(np.random.choice(second))])
    payment_method = np.random.choice(['Cash','Card'])
    week_day = np.random.choice(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    sqlFormula = """INSERT INTO transact (total_cost,trans_date,trans_time,week_day,payment_method) 
                    VALUES ({},'{}','{}','{}','{}')""".format(total_cost,trans_date,trans_time,week_day,payment_method)
    mycursor.execute(sqlFormula)
    card_id = np.random.choice(cardAll)
    store_id = np.random.choice(storeAll)
    for j in range(np.random.choice(range(100))):
        barcode = np.random.choice(ab['barcode'])
        quantity = np.random.choice(range(1,6))
        sqlFormula = """INSERT INTO bought (transact_id,card_id,store_id,quantity,barcode)
                    VALUES ({},{},{},{},{})""".format(i+1,card_id,store_id,quantity,barcode)
        mycursor.execute(sqlFormula)
    mydb.commit()
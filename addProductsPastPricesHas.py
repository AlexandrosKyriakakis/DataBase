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
shelfAlleyAll = np.arange(1,100,1)
year,month,day = np.arange(1970,2019,1), np.arange(1,12,1), np.arange(1,29,1)
hour,minute,second = np.arange(10,23,1), np.arange(10,59,1), np.arange(10,59,1)
for i in range(len(ab)):
    barcode = ab['barcode'][i] #FIXME
    category = ab['category'][i]
    name = ab['name'][i].replace('"','').replace("'",'')
    producer = ab['producer'][i].replace('"','').replace("'",'')
    price = ab['price'][i].replace(',','.')
    specialNote = 1 if (producer in ['ΑΒ','ΑΒ ΒΙΟ','ΑΒ ΕΠΙΛΟΓΗ','ΑΒ FRESH TO GO'])  else 0
    sqlFormula = """INSERT INTO product (barcode, product_name, producer_name, price, special_note, category) 
                    VALUES ('{}','{}','{}','{}',b'{}','{}')""".format(barcode,name,producer,price,specialNote,category)
    mycursor.execute(sqlFormula)
    mydb.commit()
    for j in range(np.random.choice(range(1,10))):
        sqlFormula = """INSERT INTO past_prices (barcode,past_price,time_of_change)
                        VALUES ({},{},'{}')""".format(barcode,float(price) + np.random.choice(range(1,15)),str(np.random.choice(year))+'-'+str(np.random.choice(month))+'-'+str(np.random.choice(day))+' '+str(np.random.choice(hour))+':'+str(np.random.choice(minute))+':'+str(np.random.choice(second)) )
        mycursor.execute(sqlFormula) 
    mydb.commit()
    for j in range(1,np.random.choice(range(1,12))):
        sqlFormula = """INSERT INTO has (store_id,barcode,shelf,alley)
                        VALUES ({},{},{},{})""".format(j,barcode,np.random.choice(shelfAlleyAll),np.random.choice(shelfAlleyAll))
        mycursor.execute(sqlFormula)
    mydb.commit()

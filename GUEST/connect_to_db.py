
  cur = mysql.connection.cursor()
  cur.execute('''SELECT * FROM customer''')
  results = cur.fetchall()
 # print (results)

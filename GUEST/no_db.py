import os
from flask import Flask, render_template
from flask import request
app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/')
def mainIndex():
    return render_template('index.html', selectedMenu='Home')

@app.route('/report')
def report():
  return render_template('report.html', selectedMenu='Report')

@app.route('/report2', methods=['POST'])
def report2():

  abduction = {'firstname': request.form['firstname'],
               'lastname': request.form['lastname']}
  return render_template('report2.html', abduction = abduction)

@app.route('/simple')
def simple():
  return render_template('simple.html')

@app.route('/simple2', methods=['POST'])
def simple2():
  return render_template('simple2.html')


@app.route('/simple3')
def simple3():
  return render_template('simple3.html')

@app.route('/simple4', methods=['POST'])
def simple4():
  return render_template('simple4.html', name=request.form['name'])

@app.route('/fleet')
def showChart():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("SELECT	make,model,type,cylinder_capacity,horse_power,fuel_type,year,kilometers FROM vehicle ORDER BY make,vehicle.type,model")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('fleet.html', albums=results)

@app.route('/Car_Dodge')
def Car_Dodge():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Dodge' and vehicle.type = 'Car')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Car_Honda')
def Car_Honda():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Honda' and vehicle.type = 'Car')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Car_Jeep')
def Car_Jeep():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Honda' and vehicle.type = 'Car')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Car_Toyota')
def Car_Toyota():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Toyota' and vehicle.type = 'Car')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Car_Volkswagen')
def Car_Volkswagen():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='VW' and vehicle.type = 'Car')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Moto_Honda')
def Moto_Honda():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Honda' and vehicle.type = 'Motorcycle')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Moto_Yamaha')
def Moto_Yamaha():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Yamaha' and vehicle.type = 'Motorcycle')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/ATV_Jeep')
def ATV_Jeep():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Jeep' and vehicle.type = 'ATV')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Mini_Dodge')
def Mini_Dodge():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Dodge' and vehicle.type = 'Mini Van')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Mini_Jeep')
def Mini_Jeep():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Jeep' and vehicle.type = 'Mini Van')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Mini_Toyota')
def Mini_Toyota():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Toyota' and vehicle.type = 'Mini Van')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Mini_VW')
def Mini_VW():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='VW' and vehicle.type = 'Mini Van')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/Truck_Toyota')
def Truck_Toyota():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select distinct make,model,horse_power,cylinder_capacity,year from vehicle,rents,reserves where ((vehicle.license_plate = rents.license_plate ) and ( vehicle.license_plate=reserves.license_plate) and (rents.finish_date < clock_timestamp()) and (reserves.finish_date < clock_timestamp()) and vehicle.make='Toyota' and vehicle.type = 'Truck')")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('vehiclePrototype.html', albums=results)

@app.route('/contact_us')
def ShowContacts():
  """rows returned from postgres are just an ordered list"""

  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("SELECT street, street_number, city, postal_code, email ,phone FROM store ORDER BY city;")
  except:
  	print("Error executing select")
  results = cur.fetchall()
  return render_template('contact_us.html', albums=results)


@app.route('/music2')
def showChartUsingPythonDictionary():
  """rows returned from postgres are a python dictionary (can
  also be treated as an ordered list)"""
  conn = connectToDB()
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  try:
    cur.execute("select artist, name from albums")
  except:
    print("Error executing select")
  results = cur.fetchall()
  print ("FACTORY")
  print (results)
  return render_template('music2.html', albums=results)


@app.route('/music3', methods=['GET', 'POST'])
def showChartForms():
  """rows returned from postgres are a python dictionary (can
  also be treated as an ordered list)"""
  conn = connectToDB()
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  if request.method == 'POST':
    # add new entry into database
    try:
      cur.execute("""INSERT INTO albums (artist, name, rank)
       VALUES (%s, %s, %s);""",
       (request.form['artist'], request.form['album'], request.form['rank']) )
    except:
      print("ERROR inserting into albums")
      print("Tried: INSERT INTO albums (artist, name, rank) VALUES ('%s', '%s', %s);" %
        (request.form['artist'], request.form['album'], request.form['rank']) )
      conn.rollback()
    conn.commit()

  try:
    cur.execute("select artist, name from albums")
  except:
    print("Error executing select")
  results = cur.fetchall()
  print (results)
  #for r in results:
   # print r['artist']
  return render_template('music3.html', albums=results)



#if __name__ == '__main__':
#    app.debug=True
 #   app.run(host='0.0.0.0', port=8080)



@app.route('/shutdown')
def shutdown():
    shutdown_server()
    psycopg2.close()
    return 'Server shutting down...'

# start the server
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8587)), debug=True)

import os
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_USER"] = "Giannis"
app.config["MYSQL_PASSWORD"] = "el17001el12163"
app.config["MYSQL_HOST"] = "db-ece-ntua.cqkzf2d0epmt.us-east-2.rds.amazonaws.com"
app.config["MYSQL_DB"] = "AlexJohnChris"
mysql = MySQL(app)


def shutdown_server():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()


@app.route("/")
def mainIndex():
    return render_template("layout.html")


@app.route("/search")
def search():
    return render_template("index.html")


@app.route("/search_result", methods=["GET", "POST"])
def search_result():
    my_data = request.get_json(force=True)
    """
  my_data.get("store") = "all stores"
  my_data.get("birthday") = ""
  my_data.get("quantity") = ""
  my_data.get("barcode") = ""
  my_data.get("total_amount") = ""
  my_data.get("payment_method") = "either"
  my_data.get("category") = "any'


  """
    storeid = (
        " and bought.store_id = {}".format(my_data.get("store"))
        if (my_data.get("store") != "")
        else ""
    )
    transdate = (
        " and transact.trans_date = '{}'".format(my_data.get("birthday"))
        if (my_data.get("birthday") != "")
        else ""
    )
    quantity = (
        " and bought.quantity >= {}".format(my_data.get("quantity"))
        if (my_data.get("quantity") != "")
        else ""
    )
    barcode = (
        " and bought.barcode = {}".format(my_data.get("barcode"))
        if (my_data.get("barcode") != "")
        else ""
    )
    total_cost = (
        " and transact.total_cost >= {}".format(my_data.get("total_amount"))
        if (my_data.get("total_amount") != "")
        else ""
    )
    payment_method = (
        " and transact.payment_method = '{}'".format(my_data.get("payment_method"))
        if (my_data.get("payment_method") != "")
        else ""
    )
    category = (
        " and bought.barcode in (select barcode from product where category = '{}')".format(
            my_data.get("category")
        )
        if (my_data.get("category") != "")
        else ""
    )
    # print("Here:", storeid)
    everything = "select transact.transact_id,transact.total_cost, transact.trans_date,transact.trans_time,transact.week_day,transact.payment_method,bought.card_id,bought.barcode,bought.quantity from transact, bought where bought.transact_id = transact.transact_id"
    cur = mysql.connection.cursor()
    my_query = (
        everything
        + storeid
        + transdate
        + quantity
        + barcode
        + total_cost
        + payment_method
        + category
        + " limit 20"
    )
    # print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    # the_id = request.args.get('button_id')
    return render_template("music.html", albums=results)


"""
@app.route("/customers")
def customers():
    return render_template("customers.html")
"""


@app.route("/customers", methods=["GET", "POST"])
def customerNew():
    my_data = request.get_json()
    actual_data = 0
    if my_data == None:
        actual_data = 0
    else:
        actual_data = int(my_data.get("store"))
    cur = mysql.connection.cursor()
    myquery4 = """select hour(trans_time), count(hour(trans_time))
                from transact
                where transact_id in (
	                select transact_id 
	                from bought 
                  where card_id = {}
                )
                group by hour(trans_time)
                order by hour(trans_time)""".format(
        actual_data
    )
    cur.execute(myquery4)
    # print(type(cur.fetchall()))
    result = []
    x = ("x", "y")
    for row in cur:
        result.append(dict(zip(x, row)))
    print(result)
    return render_template("customers.html", result=result)


@app.route("/customers_visit_data")
def customers():
    return render_template("customers_visit_data.html")


@app.route("/customer_result", methods=["GET", "POST"])
def customer_result():
    my_data = request.get_json(force=True)
    my_useful_data = my_data["card_id"]
    cur = mysql.connection.cursor()
    my_query_2 = "SELECT distinct b.card_id, b.store_id FROM bought as b, store as s where b.store_id = s.store_id AND b.card_id = {} order by card_id, store_id".format(
        my_useful_data
    )
    print(my_query_2)
    cur.execute(my_query_2)
    results2 = cur.fetchall()
    my_query_3 = """
SELECT 
    a.card_id, a.barcode, a.sum_quantity
FROM
    (SELECT 
        card_id, barcode, SUM(quantity) AS sum_quantity
    FROM
        bought
  WHERE card_id = {}
    GROUP BY card_id , barcode
    ORDER BY card_id , SUM(quantity) DESC) AS a
WHERE
    (SELECT 
            COUNT(*)
        FROM
            (SELECT 
                card_id, barcode, SUM(quantity) AS sum_quantity
            FROM
                bought
                WHERE card_id = {}
            GROUP BY card_id , barcode
            ORDER BY card_id , SUM(quantity) DESC) AS b
        WHERE
            (b.card_id = a.card_id
                AND b.sum_quantity > a.sum_quantity)) < 10
ORDER BY a.card_id ASC , a.sum_quantity DESC""".format(
        my_useful_data, my_useful_data
    )
    print(my_query_3)
    cur.execute(my_query_3)
    results3 = cur.fetchall()
    my_query_4 = """
    SELECT 
    b.card_id, MONTHNAME(t.trans_date), cast(AVG(t.total_cost) as decimal(6,2)) 
FROM
    transact AS t,
    bought AS b
WHERE
    b.card_id = {}
   AND b.transact_id = t.transact_id
GROUP BY MONTHNAME(t.trans_date)
ORDER BY MONTH(t.trans_date);
""".format(
        my_useful_data
    )
    print(my_query_4)
    cur.execute(my_query_4)
    results4 = cur.fetchall()
    my_query_5 = """
    SELECT 
	b.card_id,
    WEEK(t.trans_date) Week,
    cast(AVG(total_cost) as decimal(6,2))
FROM
    bought AS b,
    transact AS t
WHERE
	b.card_id = {}
    AND b.transact_id = t.transact_id
GROUP BY WEEK(t.trans_date) 
""".format(
        my_useful_data
    )
    print(my_query_5)
    cur.execute(my_query_5)
    results5 = cur.fetchall()

    # the_id = request.args.get('button_id')
    return render_template(
        "music2.html",
        results=results2,
        results3=results3,
        results4=results4,
        results5=results5,
    )


@app.route("/report2", methods=["GET", "POST"])
def report2():
    abduction = {
        "firstname": request.form["firstname"],
        "lastname": request.form["lastname"],
    }
    return render_template("report2.html", abduction=abduction)


# start the server
if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8587)), debug=True
    )

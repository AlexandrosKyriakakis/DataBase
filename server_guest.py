import os
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_USER"] = "*****"
app.config["MYSQL_PASSWORD"] = "******"
app.config["MYSQL_HOST"] = "******"
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


@app.route("/product_bought_together", methods=["GET", "POST"])
def product_bought_together():
    cur = mysql.connection.cursor()
    my_query = """SELECT 
    A.barcode, B.barcode, COUNT(A.barcode)
FROM
    bought A,
    bought B
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
GROUP BY A.barcode , B.barcode
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 100;
"""
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("music3.html", results=results)


@app.route("/popular_positions", methods=["GET", "POST"])
def popular_positions():
    cur = mysql.connection.cursor()
    my_query = """SELECT 
    A.store_id, A.shelf, A.alley, COUNT(B.barcode)
FROM
    has A,
    bought B
WHERE
    A.barcode = B.barcode
GROUP BY B.barcode , A.store_id , A.shelf , A.alley
ORDER BY COUNT(B.barcode) DESC
LIMIT 100;
"""
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("music4.html", results=results)


@app.route("/label_trust", methods=["GET", "POST"])
def label_trust():
    cur = mysql.connection.cursor()
    my_query = """SELECT
   A.category,
   COUNT(B.barcode) / E.total * 100 AS percentage
FROM
   product A,
   bought B,
   (SELECT COUNT(C.barcode) as total, D.category as categor
   FROM bought C, product D 
   WHERE C.barcode = D.barcode
   GROUP BY D.category)E
WHERE
    A.barcode = B.barcode
   and A.category = E.categor
   AND A.special_note = 1
GROUP BY A.special_note , A.category
ORDER BY percentage DESC;
"""
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("music5.html", results=results)


@app.route("/hours_spent_more", methods=["GET", "POST"])
def hours_spent_more():
    cur = mysql.connection.cursor()
    my_query = """SELECT 
    HOUR(trans_time),
    CAST(SUM(A.total_cost) AS DECIMAL (20 , 2 ))
FROM
    transact A,
    bought B
WHERE
    A.transact_id = B.transact_id
GROUP BY HOUR(trans_time)
ORDER BY SUM(A.total_cost) DESC , HOUR(trans_time)
"""
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("music6.html", results=results)


@app.route("/age_percentage", methods=["GET", "POST"])
def age_percentage():
    cur = mysql.connection.cursor()
    my_query = """
SELECT distinct
    cast(SUM(IF(A.age < 20, 1, 0))/totals.total * 100 as decimal(20,2)) AS 'Under 20',
    cast(SUM(IF(A.age BETWEEN 20 AND 29, 1, 0))/totals.total * 100  as decimal(20,2)) AS '20 - 29',
    cast(SUM(IF(A.age BETWEEN 30 AND 39, 1, 0))/totals.total * 100 as decimal(20,2)) AS '30 - 39',
    cast(SUM(IF(A.age BETWEEN 40 AND 49, 1, 0))/totals.total * 100 as decimal(20,2)) AS '40 - 49',
    cast(SUM(IF(A.age BETWEEN 50 AND 59, 1, 0))/totals.total * 100 as decimal(20,2)) AS '50 - 59',
    cast(SUM(IF(A.age BETWEEN 60 AND 69, 1, 0))/totals.total * 100 as decimal(20,2)) AS '60 - 69',
    cast(SUM(IF(A.age >= 70, 1, 0))/totals.total * 100 as decimal (20,2)) AS 'Over 70',
    HOUR(C.trans_time) AS Hour
FROM
    (SELECT distinct
        YEAR(CURDATE()) - YEAR(birth_date) - IF(STR_TO_DATE(CONCAT(YEAR(CURDATE()), '-', MONTH(birth_date), '-', DAY(birth_date)), '%Y-%c-%e') > CURDATE(), 1, 0) AS age,
            card_id
    FROM
        customer) A,
    (SELECT * from bought group by transact_id) B
    LEFT JOIN
    transact C on B.transact_id = C.transact_id,
    (SELECT distinct
        COUNT(D.transact_id) as total, HOUR(D.trans_time) as total_hour
        FROM 
            transact D
        GROUP BY HOUR(D.trans_time)
        ORDER BY HOUR(D.trans_time)) totals
WHERE
    A.card_id = B.card_id
        AND B.transact_id = C.transact_id
        AND totals.total_hour = HOUR(C.trans_time)
GROUP BY  HOUR(C.trans_time)
ORDER BY HOUR(C.trans_time)

"""
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("music7.html", results=results)


@app.route("/sales_category_store", methods=["GET", "POST"])
def sales_category_store():
    cur = mysql.connection.cursor()
    my_query = "SELECT * FROM sales_category_store"
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("music8.html", results=results)


@app.route("/customer_info", methods=["GET", "POST"])
def customer_info():
    cur = mysql.connection.cursor()
    my_query = "SELECT * FROM customer_info"
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("music9.html", results=results)


@app.route("/past_prices", methods=["GET", "POST"])
def past_prices():
    cur = mysql.connection.cursor()
    my_query = "SELECT * FROM past_prices ORDER BY time_of_change desc"
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("music10.html", results=results)


@app.route("/editStores")
def editStores():
    return render_template("editStores.html")


@app.route("/search_resultS", methods=["GET", "POST"])
def editStoresResponce():
    my_data = request.get_json(force=True)
    edit = int(my_data.get("edit"))
    print(edit)
    if edit == -1:
        store = my_data.get("store")
        if store != "":
            cur = mysql.connection.cursor()
            my_query = "DELETE FROM store WHERE store_id = {}".format(store)
            cur.execute(my_query)
            cur.fetchall()
    elif edit == 0:
        # Update ...

        data = my_data.get("phone")
        phone = " phone = '{}' ".format(data) if (data != "") else ""

        data = my_data.get("city")
        city = " city = '{}' ".format(data) if (data != "") else ""

        data = my_data.get("address")
        address = " store_address = '{}' ".format(data) if (data != "") else ""

        data = my_data.get("postal_code")
        postal_code = " postal_code = '{}' ".format(data) if (data != "") else ""

        data = my_data.get("opening_time")
        opening_time = " opening_time = '{}' ".format(data) if (data != "") else ""

        data = my_data.get("closing_time")
        closing_time = " closing_time = '{}' ".format(data) if (data != "") else ""

        data = my_data.get("square_meters")
        square_meters = " square_meters = '{}' ".format(data) if (data != "") else ""

        additionalQuery = [
            phone,
            city,
            address,
            postal_code,
            opening_time,
            closing_time,
            square_meters,
        ]
        additionalQuery = ",".join(list(filter(lambda i: i != "", additionalQuery)))
        if additionalQuery != "":
            my_query = (
                "update store set "
                + additionalQuery
                + " where store_id = {};".format(my_data.get("store"))
            )

            cur = mysql.connection.cursor()
            cur.execute(my_query)
            cur.fetchall()
    elif edit == 1:
        # Add ...
        data = my_data.get("phone")
        phone = ("phone", "'" + data + "'") if (data != "") else ""

        data = my_data.get("city")
        city = ("city", "'" + data + "'") if (data != "") else ""

        data = my_data.get("address")
        address = ("store_address", "'" + data + "'") if (data != "") else ""

        data = my_data.get("postal_code")
        postal_code = ("postal_code", "'" + data + "'") if (data != "") else ""

        data = my_data.get("opening_time")
        opening_time = ("opening_time", "'" + data + "'") if (data != "") else ""

        data = my_data.get("closing_time")
        closing_time = ("closing_time ", "'" + data + "'") if (data != "") else ""

        data = my_data.get("square_meters")
        square_meters = ("square_meters", "'" + data + "'") if (data != "") else ""

        additionalQuery = [
            phone,
            city,
            address,
            postal_code,
            opening_time,
            closing_time,
            square_meters,
        ]
        additionalQuery = list(filter(lambda i: i != "", additionalQuery))
        if additionalQuery != []:
            attributes, values = zip(*additionalQuery)
            attributes = ",".join(attributes)
            values = ",".join(values)
            my_query = "insert into store (" + attributes + ") values (" + values + ")"
            print(my_query)
            cur = mysql.connection.cursor()
            cur.execute(my_query)
            cur.fetchall()

    cur = mysql.connection.cursor()
    my_query = "select * from store"
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("editStoresResponce.html", albums=results)


@app.route("/query_2", methods=["GET", "POST"])
def query_2():
    cur = mysql.connection.cursor()
    my_query = """
    (SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 1
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 2
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 3
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 4
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 5
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 6
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 7
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 8
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 9
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
union
(SELECT 
    A.barcode,C.shelf,C.alley, B.barcode,D.shelf,D.alley, COUNT(A.barcode), A.store_id
FROM
    bought A,
    bought B,
    has C,
    has D
WHERE
    A.transact_id = B.transact_id
        AND A.barcode > B.barcode
        AND A.barcode = C.barcode
        AND A.store_id = C.store_id
        AND B.barcode = D.barcode
        AND B.store_id = 10
        AND B.store_id = D.store_id
GROUP BY A.barcode , B.barcode, A.store_id
ORDER BY COUNT(A.barcode) DESC , A.barcode , B.barcode
LIMIT 1)
    """
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("query_2.html", results=results)


@app.route("/query_1", methods=["GET", "POST"])
def query_1():
    cur = mysql.connection.cursor()
    my_query = """
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store_id = h.store_id 
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Φρέσκα Προϊόντα'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store_id = h.store_id 
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Ποϊόντα Ψυγείου'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store_id = h.store_id 
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Κατοικίδια'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store_id = h.store_id 
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Κάβα'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store_id = h.store_id 
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Είδη Σπιτιού'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store_id = h.store_id 
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Προσωπικής Περιποίησης'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store_id = h.store_id 
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Είδη Σπιτιού'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
"""
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("query_1.html", results=results)


@app.route("/editProducts")
def editProducts():
    return render_template("editProducts.html")


@app.route("/search_resultP", methods=["GET", "POST"])
def editProductsResponce():
    my_data = request.get_json(force=True)
    edit = int(my_data.get("action"))
    print(edit)
    if edit == -1:
        barcode = my_data.get("barcode")
        if barcode != "":
            cur = mysql.connection.cursor()
            my_query = "DELETE FROM product WHERE barcode = {}".format(barcode)
            cur.execute(my_query)
            mysql.connection.commit()
    elif edit == 0:
        # Update ...

        data = my_data.get("product_name")
        product_name = " product_name = '{}' ".format(data) if (data != "") else ""

        data = my_data.get("producer_name")
        producer_name = " producer_name = '{}' ".format(data) if (data != "") else ""

        data = my_data.get("price")
        price = " price = '{}' ".format(data) if (data != "") else ""

        data = my_data.get("special_note")
        special_note = " special_note = b'{}' ".format(data) if (data != "") else ""

        data = my_data.get("category")
        category = " category = '{}' ".format(data) if (data != "") else ""

        additionalQuery = [
            product_name,
            producer_name,
            price,
            special_note,
            category,
        ]
        additionalQuery = ",".join(list(filter(lambda i: i != "", additionalQuery)))
        if additionalQuery != "":
            my_query = (
                "update product set "
                + additionalQuery
                + " where barcode = {};".format(my_data.get("barcode"))
            )

            cur = mysql.connection.cursor()
            cur.execute(my_query)
            mysql.connection.commit()
    elif edit == 1:
        # Add ...
        data = my_data.get("barcode")
        barcode = ("barcode", "'" + data + "'") if (data != "") else ""

        data = my_data.get("product_name")
        product_name = ("product_name", "'" + data + "'") if (data != "") else ""

        data = my_data.get("producer_name")
        producer_name = ("producer_name", "'" + data + "'") if (data != "") else ""

        data = my_data.get("price")
        price = ("price", "'" + data + "'") if (data != "") else ""

        data = my_data.get("special_note")
        special_note = ("special_note", "b'" + data + "'") if (data != "") else ""

        data = my_data.get("category")
        category = ("category", "'" + data + "'") if (data != "") else ""

        additionalQuery = [
            barcode,
            product_name,
            producer_name,
            price,
            special_note,
            category,
        ]
        additionalQuery = list(filter(lambda i: i != "", additionalQuery))
        if additionalQuery != []:
            attributes, values = zip(*additionalQuery)
            attributes = ",".join(attributes)
            values = ",".join(values)
            my_query = (
                "insert into product (" + attributes + ") values (" + values + ")"
            )
            print(my_query)
            cur = mysql.connection.cursor()
            cur.execute(my_query)
            mysql.connection.commit()

    cur = mysql.connection.cursor()
    my_query = "select * from product"
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("editProductsResponce.html", albums=results)


@app.route("/editCustomers")
def editCustomers():
    return render_template("editCustomers.html")


@app.route("/search_resultC", methods=["GET", "POST"])
def editCustomersResponce():
    my_data = request.get_json(force=True)
    edit = int(my_data.get("edit"))
    print(edit)
    if edit == -1:
        card_id = my_data.get("card_id")
        if card_id != "":
            cur = mysql.connection.cursor()
            my_query = "DELETE FROM customer WHERE card_id = {}".format(card_id)
            cur.execute(my_query)
            mysql.connection.commit()
    elif edit == 0:
        card_id = my_data.get("card_id")
        if card_id != "":
            # Update ...

            data = my_data.get("first_name")
            first_name = " first_name = '{}' ".format(data) if (data != "") else ""

            data = my_data.get("last_name")
            last_name = " last_name = '{}' ".format(data) if (data != "") else ""

            data = my_data.get("total_points")
            total_points = " total_points = '{}' ".format(data) if (data != "") else ""

            data = my_data.get("rewards")
            rewards = " rewards = '{}' ".format(data) if (data != "") else ""

            data = my_data.get("birthdate")
            birthdate = " birth_date = '{}' ".format(data) if (data != "") else ""

            data = my_data.get("marital_status")
            marital_status = (
                " marital_status = '{}' ".format(data) if (data != "") else ""
            )

            data = my_data.get("social_security_number")
            social_security_number = (
                " social_security_number = '{}' ".format(data) if (data != "") else ""
            )

            phone_number = my_data.get("phone_number")
            if phone_number != "":
                editNumber = int(my_data.get("editNumber"))
                phone_number = phone_number.split(",")
                if editNumber == -1:
                    my_query = "DELETE FROM customer_phone WHERE card_id = {} and phone_number in ({});".format(
                        card_id, ",".join(phone_number)
                    )
                    cur = mysql.connection.cursor()
                    cur.execute(my_query)
                    mysql.connection.commit()
                elif editNumber == 1:
                    for phone in phone_number:
                        my_query = "insert into customer_phone  (card_id,phone_number) values ('{}','{}');".format(
                            card_id, phone
                        )
                        cur = mysql.connection.cursor()
                        cur.execute(my_query)
                        mysql.connection.commit()

            additionalQuery = [
                first_name,
                last_name,
                total_points,
                rewards,
                birthdate,
                marital_status,
                social_security_number,
            ]
            additionalQuery = ",".join(list(filter(lambda i: i != "", additionalQuery)))
            if additionalQuery != "":
                my_query = (
                    "update customer set "
                    + additionalQuery
                    + " where card_id = {};".format(my_data.get("card_id"))
                )

                cur = mysql.connection.cursor()
                cur.execute(my_query)
                mysql.connection.commit()
    elif edit == 1:
        # Add ...
        data = my_data.get("first_name")
        first_name = ("first_name", "'" + data + "'") if (data != "") else ""

        data = my_data.get("last_name")
        last_name = ("last_name", "'" + data + "'") if (data != "") else ""

        data = my_data.get("total_points")
        total_points = ("total_points", "'" + data + "'") if (data != "") else ""

        data = my_data.get("rewards")
        rewards = ("rewards", "'" + data + "'") if (data != "") else ""

        data = my_data.get("birth_date")
        birth_date = ("birth_date", "'" + data + "'") if (data != "") else ""

        data = my_data.get("marital_status")
        marital_status = ("marital_status ", "'" + data + "'") if (data != "") else ""

        data = my_data.get("social_security_number")
        social_security_number = (
            ("social_security_number", "'" + data + "'") if (data != "") else ""
        )

        additionalQuery = [
            first_name,
            last_name,
            total_points,
            rewards,
            birth_date,
            marital_status,
            social_security_number,
        ]
        additionalQuery = list(filter(lambda i: i != "", additionalQuery))
        if additionalQuery != []:
            attributes, values = zip(*additionalQuery)
            attributes = ",".join(attributes)
            values = ",".join(values)
            my_query = (
                "insert into customer (" + attributes + ") values (" + values + ")"
            )
            print(my_query)
            cur = mysql.connection.cursor()
            cur.execute(my_query)
            mysql.connection.commit()

            phone_number = my_data.get("phone_number")
            if phone_number != "":
                editNumber = int(my_data.get("editNumber"))
                phone_number = phone_number.split(",")
                if editNumber == 1:
                    card = "select max(card_id) from customer;"
                    cur = mysql.connection.cursor()
                    cur.execute(card)
                    card_id = cur.fetchall()[0][0]
                    mysql.connection.commit()
                    for phone in phone_number:
                        my_query = "insert into customer_phone  (card_id,phone_number) values ('{}','{}');".format(
                            card_id, phone
                        )
                        print(my_query)
                        cur = mysql.connection.cursor()
                        cur.execute(my_query)
                        mysql.connection.commit()

    cur = mysql.connection.cursor()
    my_query = "select A.*, B.phone_number from customer A, customer_phone B where B.card_id = A.card_id;"
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("editCustomersResponce.html", albums=results)


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
        " and month(transact.trans_date) = month('{0}') and year(transact.trans_date) = year('{0}')".format(
            my_data.get("birthday")
        )
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
        + " limit 1000"
    )
    print(my_query)
    cur.execute(my_query)
    results = cur.fetchall()
    return render_template("music.html", albums=results)


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
        SELECT card_id, barcode, sum(quantity)
        FROM bought
        where card_id = {}
        group by barcode
        order by sum(quantity) desc
        limit 10
        """.format(
        my_useful_data
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

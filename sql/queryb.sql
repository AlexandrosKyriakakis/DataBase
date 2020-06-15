use AlexJohnChris;
SELECT 
    a.card_id, a.barcode, a.sum_quantity
FROM
    (SELECT 
        card_id, barcode, SUM(quantity) AS sum_quantity
    FROM
        bought
	WHERE card_id = 1
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
                WHERE card_id = 1
            GROUP BY card_id , barcode
            ORDER BY card_id , SUM(quantity) DESC) AS b
        WHERE
            (b.card_id = a.card_id
                AND b.sum_quantity >= a.sum_quantity)) < 10
ORDER BY a.card_id ASC , a.sum_quantity DESC
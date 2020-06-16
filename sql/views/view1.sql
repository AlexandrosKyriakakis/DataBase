use AlexJohnChris;
CREATE VIEW sales_category_store
AS
SELECT B.transact_id, B.card_id, H.barcode, B.quantity, P.category, H.store_id
FROM
bought B, has H, product P
WHERE B.barcode = H.barcode
AND H.barcode = P.barcode
ORDER BY P.category, H.store_id

(select p.category, h.store*id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store*id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Φρέσκα Προϊόντα'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store*id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Ποϊόντα Ψυγείου'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store*id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Κατοικίδια'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store*id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Κάβα'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)
UNION
(select p.category, h.store_id, COUNT(*) as counter
FROM product p, has h, bought b
WHERE b.store*id = h.store_id
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
(select p.category, h.store_id, COUNT(\*) as counter
FROM product p, has h, bought b
WHERE b.store_id = h.store_id
AND h.barcode = b.barcode
AND h.barcode = p.barcode
AND p.category = 'Είδη Σπιτιού'
GROUP BY h.store_id
ORDER BY counter desc
limit 1)

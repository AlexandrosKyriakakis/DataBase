use AlexJohnChris;
DELIMITER //
DROP TRIGGER IF EXISTS past_p//
CREATE TRIGGER past_p AFTER UPDATE 
ON product 
FOR EACH ROW
BEGIN
IF (not NEW.price <=> OLD.price) THEN 
INSERT INTO past_prices (barcode,past_price,time_of_change) 
VALUES (OLD.barcode, OLD.price, NOW());
END IF;
END;//
DELIMITER ;
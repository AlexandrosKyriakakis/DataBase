use AlexJohnChris;
CREATE VIEW customer_info
AS
SELECT DISTINCT c.card_id, c.first_name, c.last_name, c.total_points, c.rewards, c.birth_date, c.marital_status, c.social_security_number, c.sex, p.phone_number
FROM
customer c 
LEFT JOIN
customer_phone p
on c.card_id = p.card_id



1. List the stores allowed to sell alcohol
	Select id, name 
		from interview.stores
		where allowed_alcohol = true;

	id	name
	1	Gettar

2. Give the product name of the 2 most expensive items based on their price at store id 1

	Note for table "interview.store_prices" I changed data type of 'price' from numeric to numeric(3,2) without that both price of id 1 and 2 were getting rounded off to '3'

	SELECT p.name, s.price
    FROM interview.store_prices s join interview.products p on p.id = s.product_id
    where s.store_id = 1
    ORDER BY s.price DESC
    LIMIT 2;

	name price
	'Golden Banana','3.59'
	'Banana','3.32'


3. List the products that are not sold in the store id 2
	SELECT p.name, p.id 
	FROM interview.products p 
	WHERE p.id NOT IN 
	(
		SELECT product_id 
		FROM interview.store_prices as s
		where s.store_id = 2 
		AND s.product_id is not null
	)

	ANSWER : 

	name id
	'Banana','2'
	'Golden Banana','4'
	'Bouquet Flowers','5'

4. What is the most popular item sold?
	SELECT p.name, p.id
	FROM interview.products p 
  	JOIN 
  		(SELECT product_id, SUM(qty) AS TotalQuantity
			FROM interview.order_lines 
			GROUP BY product_id
			ORDER BY SUM(qty) DESC
			LIMIT 1
		) AS omax
    ON p.id = omax.product_id

    ANSWER : 
	name id
	'Banana','2'

5. Write a SQL statement to update the line_total field
	UPDATE interview.order_lines 
	SET line_total = 2 
	WHERE product_id = 3;
	SELECT * FROM interview.order_lines;

	id product_id store_id qty line_total
	'1','1','2','3',NULL
	'2','2','1','50',NULL
	'3','2','1','1',NULL
	'4','3','2','4','2'
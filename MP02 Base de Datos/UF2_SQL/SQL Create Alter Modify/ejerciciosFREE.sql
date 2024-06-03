use callcenter_prueba;
-- 2 INSERTS

	-- 1 
INSERT INTO city (city_name) VALUES ('Manresa'),('Berga'),('El Prat de Llobregat');

-- 2 
UPDATE customer SET city_id = (select id from city where city_name = 'Manresa') WHERE city_id = (select id from city where city_name = 'Barcelona');

-- 3 
DELETE FROM phone_call where call_outcome_id = (
           select id from call_outcome 
		   where outcome_text ='finished - unsuccessfully');
           
-- 4.1 
INSERT INTO employee (first_name, last_name) VALUES ('William', 'Molina Galan');

-- 4.2 
INSERT INTO phone_call (employee_id, customer_id, start_time)
SELECT (SELECT id FROM employee WHERE first_name = 'William' AND last_name = 'Molina Galan') AS employee_id,
	c.id as customer_id, NOW() as start_time
FROM customer c JOIN city cy on c.city_id = cy.id
WHERE city_name = 'Manresa';


-- Por si a mi yo del futuro se le pasa mirar una CONSTRAINT DE CHECK
-- ALTER TABLE call_outcome ADD CONSTRAINT outcome_text CHECK (outcome_text IN ('call started','finished - successfully','finished - unsuccessfully'));

-- SET SQL_SAFE_UPDATES = 1;
-- DELETE from phone_call where id IN 
-- (select id from (select id where start_time= '2024-01-29 00:43:50')AS subquery);



-- 3
	-- 3.1
ALTER TABLE phone_call
ADD CONSTRAINT employee_call_unique
UNIQUE (employee_id, start_time);
-- Si no deja: ya existen registros de llamadas con datos duplicados en la tabla phone_call
-- donde un trabajador ha hecho mas de una llamada en la misma hora. Para aplicar UNIQUE es necesario borrar
-- los datos duplicados

	-- 3.2   (PROBAR CON ENUM PARA VER SI NO DA TANTOS PROBLEMAS)
ALTER TABLE phone_call
ADD COLUMN first_time VARCHAR(3)
CHECK (first_time IN ('YES','NO'));     





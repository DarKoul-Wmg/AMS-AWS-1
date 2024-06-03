-- 1
INSERT INTO animal (name, species, birth_date) VALUES 
('Laika','gos','2023-01-22'),('Miau','gat','2023-01-22');
-- 2
UPDATE animal SET owner_id = (select id from owner where first_name = 'Jane' AND last_name ='Smith') 
WHERE name IN ('Laika','Miau'); 

-- 3
DELETE FROM animal where id NOT IN (select animal_id from appointment);
-- 4
INSERT INTO veterinarian (first_name, last_name) VALUES ('William', 'Molina Galan');

INSERT INTO appointment (veterinarian_id, animal_id, appointment_date)
SELECT (
select id from veterinarian where first_name ='William' AND last_name = 'Molina Galan') as veterinarian_id,
a.id as animal_id, '2024-01-22' as appointment_date
FROM animal a
WHERE species ='Gat';

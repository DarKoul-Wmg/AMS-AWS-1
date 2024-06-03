SET SERVEROUTPUT ON;

/*Ejercicio 3 (2 punto) - BBDD HR
Sobre las tablas de la BBDD HR, el usuario introduce un número del 1 al 4 y se deben mostrar cuantos departamentos hay en las primeras 
x(numero introducido) regiones ( Las regiones tienen números correlativos como PK).
*/

SELECT
    * FROM departments;
    
SELECT
    * FROM regions; /* introduce los num de los departamentos  */
    
SELECT
    * FROM countries;
    
SELECT
    * FROM locations;




select count(region_id) from countries where region_id = '1';
select count(region_id) from countries where region_id = '2';
select count(region_id) from countries where region_id = '3';
select count(region_id) from countries where region_id = '4';

/*Resulado: La region x tiene este numero de departamentos  */
DECLARE 

numdepart INT;

BEGIN
numdepart:=&numdepart;

for i in  (select count(region_id) from countries where region_id ='numdepart' ) 


LOOP
dbms_output.put_line('La region '|| i.numdepart || 'tiene este num de departamantos'|| i.count(region_id) );

END LOOP;
END;
SET SERVEROUTPUT ON;

SELECT
    * FROM employees;

SELECT
    * FROM departments;
    
SELECT salary , first_name from employees where department_id = '100';

select count(first_name) from employees where department_id = '20';



    
/*
1- Bloque PL/SQL que devuelva el salario de un departamento, introducido por el usuario (department_id).

Controlar que el departamento no sea negativo y que exista.

La salida ha de mostrar lo siguiente:

Ejemplo datos ficticios:

20 - Marketing - El salario medio de este departamento es de 21000.

*/    
 
    
    
DECLARE


BEGIN






END;
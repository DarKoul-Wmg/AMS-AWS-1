SET SERVEROUTPUT ON;


--- eje 1 ---
DECLARE

departament VARCHAR2(30) := '';

BEGIN

SELECT departments.department_name into departament FROM employees inner join departments on employees.department_id = departments.department_id  where (employees.first_name = 'Pat')  ;
DBMS_OUTPUT.PUT_LINE('El departamento de Pat Fay es : '|| departament );

END;

/*
--- eje 2 ---

DECLARE

ID INT;

BEGIN

ID := &ID

DBMS_OUTPUT.PUT_LINE('Dime tu ID '|| ID ||' );

END;

*/


/*
--- eje 3 ---

DECLARE
 
imprimir varchar (40) := ';

BEGIN;

END;    

*/



--- eje 4 ---

DECLARE 

num1 := 10.2
num2 := 20.1

BEGIN;


END;


/*

--- Eje 6: 
--- eup employes%rowtype
--- dep departamentos.dep-name % type
--- pecenta constant 
---select nombre, apellido,n-departa, salary, into eup.nombre, eup.apelli, dept, eup.salary


*/





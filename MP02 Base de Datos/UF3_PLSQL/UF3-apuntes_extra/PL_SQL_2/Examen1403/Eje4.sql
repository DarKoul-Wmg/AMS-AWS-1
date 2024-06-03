SET SERVEROUTPUT ON;

/*Ejercicio 4 

Ejercicio de Cifrado. Tabla employees de HR. Queremos generar un password seguro para un trabajador introducido por el usuario y que exista.
La contraseña tiene que ser las 2 primeras letra del nombre en mayusculas, la última letra del apellido en minusculas, numero de empleado*3,departamento,@.

Ejemplo de mensaje de salida:

Hola Steven King, tu password es STg30090@.

Si no existe devolver mensaje de que no existe el empleado.
*/
SELECT UPPER(LAST_NAME), INITCAP(FIRST_NAME) from employees;



SELECT
    * FROM employees;
    
/* Contraseña  */
select UPPER(first_name), SUBSTRING(LAST_NAME, 1, 1) from employees;
select DEPARTMENT_ID*3  from employees  ;
    
/* Compro si existe ese el usu introducido, crear contra las dos primeras letras en mayus y la ultima letra del apellido en minus  */ 

DECLARE
existe number;
emplo employees.employee_id%TYPE;


BEGIN
emplo :=&emplo;
select count(employee_id) into existe from employees where employee_id=emplo;

/* 
Creamos un if que compruebe en la tabla de employees si el id seleccionado por el usuario no 
existe mande un error 

if employee_id not *existe*  then 

DBMS_OUTPUT.PUT_LINE('Error este usuario no existe ');


ELSE 

Creamos la contraseña 

despues insertamos en la tabla la nueva contraseña

insert into employees(contraseña ) values contra 


END IF;
*/

END;
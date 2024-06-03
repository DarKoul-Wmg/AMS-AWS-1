SET SERVEROUTPUT ON;
/*En este ejercicio vais a intentar insertar datos en la tabla JOBS:

Se le pedirá al usuario los siguientes datos:

job_id
job_tittle
min_salary
max_salary

realizar las siguientes comprobaciones antes de insertar:
El job_id tiene que estar entre 5 y 10 y no debe de existir ya en la base de datos.

el job_tittle debe de estar entre 5 y 35 y no debe de existir en la base de datos.

el salario minimo no puede ser negativo

el salario máximo no puede ser negativo

el salario máximo ha de ser mayor que el salario mínimo.

Si esto se cumple, realizar un insert en la tabla jobs de los datos introducidos por el usuario.
*/

SELECT * FROM jobs;

DECLARE
j_id jobs.job_id%TYPE;
j_tit jobs.job_title%TYPE;
min_sal jobs.min_salary%TYPE;
max_sal jobs.max_salaryn_salary%TYPE;
existe number;
existe2 number;

BEGIN
j_id :=&j_id;
j_tit :=&j_tit;
max_sal :=&max_sal;
min_sal :=&min_sal;


select COUNT(job_id) into existe FROM jobs where job_id=j_id;
select COUNT(job_title) into existe2 FROM jobs where job_title=j_tit;

IF lenght(j_id) not BETWEEN 5 AND 10 then
DBMS_OUTPUT.PUT_LINE('Error, es mas grande');
ELSIF existe= 1 then
DBMS_OUTPUT.PUT_LINE('Error '); 

if lenght(j_tit) not BETWEEN 5 AND 35 then
DBMS_OUTPUT.PUT_LINE('Error, es mas grande');
ELSIF existe2= 1 then
DBMS_OUTPUT.PUT_LINE('Error ');

ELSIF min_salary < 0 then
DBMS_OUTPUT.PUT_LINE('No puede ser negativo');

ELSIF max_salary < 0 then
DBMS_OUTPUT.PUT_LINE('No puede ser negativo');

else
insert into jobs(job_id,job_title_min_salry,max_salary) VALUES (j_id,j_tit,min_sal,max_sal);
END IF; 
END; 

SELECT * FROM jobs;
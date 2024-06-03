SET SERVEROUTPUT ON

/*
Realitza un procediment anomenat “dinoman” que mostri el nom de l'empleat més
antic de cada departament juntament amb el nom del departament. 
Tracta les excepcions que consideris necessàries.  
Realitza el bloc anònim corresponent per cridar al procediment.
•	Nota: Crear i Fer servir una funció anomenada old_emp per calcular l’empleat
    més antic d’un departament i cridar-lo dins el procediment
*/
select * from job_history;
select * from employees;
SELECT * FROM departments;
SELECT DEPARTMENT_ID, DEPARTMENT_NAME FROM departments;


select first_name, hire_date, department_id from employees;


create or replace FUNCTION old_emp(end_j job_history.end_date%TYPE)
return date
is
begin
return();
end;

create or replace procedure dinoman(olf_emp)
is 
begin
select employee_id, end_date from job_history;
end;




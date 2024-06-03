Set SERVEROUTPUT on;
/* 
Programar un script (exercici3.sql) que contenga un procedimiento que dé de alta un nuevo oficio (puesto de trabajo). 
Los datos del nuevo oficio se tienen que introducir por teclado. 
Antes de insertar se tiene que comprobar que el valor mínimo y máximo del oficio no sea negativo y además, que el salario mínimo sea más pequeño que el máximo.
*/
select * from jobs;

create or replace PROCEDURE oficio(j_id jobs.job_id%TYPE,j_t jobs.job_title%TYPE, sal_min jobs.min_salary%type , sal_max jobs.max_salry%type) 
is
existe number;
begin


select count(*) into existe from jobs where job_id=j_id;
if existe = 1 then 
dbsm.
else
insert into jobs values (j_id,j_t,salmin,sal_max);

end;
Set SERVEROUTPUT on;
/*
Programar un script (exercici5.sql) que contenga una funci�n que devuelva cu�ntos empleados hay de un departamento,
que se pasar� por par�metro a la funci�n. La funci�n llamada CONTAR, 
se llamar� desde un bloque an�nimo o principal y el par�metro que se le pasa a la funci�n se le preguntar� al usuario
y por tanto, se tiene que introducir por teclado.
*/

create or replace function Contar(id_dep number) return number
is 
cont number;
begin
select count(*) into cont from employees where employee_id=id_dep;
end;
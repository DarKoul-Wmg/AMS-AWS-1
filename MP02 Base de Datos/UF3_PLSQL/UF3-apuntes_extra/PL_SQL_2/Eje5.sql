Set SERVEROUTPUT on;
/*
Programar un script (exercici5.sql) que contenga una función que devuelva cuántos empleados hay de un departamento,
que se pasará por parámetro a la función. La función llamada CONTAR, 
se llamará desde un bloque anónimo o principal y el parámetro que se le pasa a la función se le preguntará al usuario
y por tanto, se tiene que introducir por teclado.
*/

create or replace function Contar(id_dep number) return number
is 
cont number;
begin
select count(*) into cont from employees where employee_id=id_dep;
end;
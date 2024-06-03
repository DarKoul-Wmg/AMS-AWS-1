/* Programar un script (exercici3.sql) que contenga un procedimiento que dé de alta un nuevo oficio (puesto de trabajo).
Los datos del nuevo oficio se tienen que introducir por teclado.
Antes de insertar se tiene que comprobar que el valor mínimo y máximo del oficio no sea negativo y además, que el salario mínimo sea más pequeño que el máximo. */

select * from employees;

create or replace NONEDITIONABLE PROCEDURE puesto_de_trabajo()
is 
begin 
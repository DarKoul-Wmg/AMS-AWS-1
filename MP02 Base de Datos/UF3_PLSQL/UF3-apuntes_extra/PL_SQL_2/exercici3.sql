/* Programar un script (exercici3.sql) que contenga un procedimiento que d� de alta un nuevo oficio (puesto de trabajo).
Los datos del nuevo oficio se tienen que introducir por teclado.
Antes de insertar se tiene que comprobar que el valor m�nimo y m�ximo del oficio no sea negativo y adem�s, que el salario m�nimo sea m�s peque�o que el m�ximo. */

select * from employees;

create or replace NONEDITIONABLE PROCEDURE puesto_de_trabajo()
is 
begin 
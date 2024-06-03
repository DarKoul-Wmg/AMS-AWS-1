/* Ejercicio 1 */

SET SERVEROUTPUT ON;

create or replace PROCEDURE listarNumeros(nume int)
is 
begin 
if (nume>0) then
    for i in 0 .. nume loop
    dbms_output.put_line(i);
    end loop;
else
dbms_output.put_line('numero incorrecto' );
end if;
end listarNumeros;
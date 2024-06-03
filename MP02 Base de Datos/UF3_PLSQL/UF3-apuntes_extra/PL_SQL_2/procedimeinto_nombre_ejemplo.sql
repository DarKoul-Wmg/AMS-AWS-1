SET SERVEROUTPUT ON
declare
nombre employees.first_name%type;
apellido employees_temp.last_name%TYPE
begin
obtener_nombre(100,nombre,apellido);
dbms_output.put_line(nombre|| ' ' || apellido);
end;

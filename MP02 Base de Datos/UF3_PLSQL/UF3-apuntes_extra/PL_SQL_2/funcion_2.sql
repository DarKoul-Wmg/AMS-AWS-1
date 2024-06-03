create or replace FUNCTION funcion_2 (e_id employees.employee_id%TYPE)
RETURN number 
is

begin
RETURN (e_id+1000);
end;
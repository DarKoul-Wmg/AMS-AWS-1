set serveroutput on;

create or replace function nom (ide employees.employee_id%type) return employees.first_name%type
is
    nombre employees.first_name%TYPE;
begin
    select first_name into nombre from employees where employee_id = ide;
    return nombre;
end;
/


declare
    nombre employees.first_name%TYPE;
    
    nulo exception;
begin
    select nom(&num) into nombre from dual;
    if nombre is null then
        raise nulo;
    else
        dbms_output.put_line('El nombre es: ' || nombre);
    end if;

exception
when nulo then
    dbms_output.put_line('No se encontro al empleado');
end;
/


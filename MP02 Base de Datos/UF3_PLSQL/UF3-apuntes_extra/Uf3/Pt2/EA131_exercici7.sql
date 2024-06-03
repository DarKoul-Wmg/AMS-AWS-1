set serveroutput on;

create or replace procedure department_a (ide departments.department_id%TYPE)
is
    nombre_dept departments.department_name%type;
    
    nocontieneA exception;
begin
    select department_name into nombre_dept from departments where department_id = ide;
    if lower(substr(nombre_dept,1,1)) = 'a' then
        dbms_output.put_line(nombre_dept || chr(10) || 'COMENÇA PER LA LLETRA A');
    else
        raise nocontieneA;
    end if;
exception
when no_data_found then
    dbms_output.put_line('ERROR: no dades');
when too_many_rows then
    dbms_output.put_line('ERROR: retorna més files');
when nocontieneA then
    dbms_output.put_line('El nombre es: ' || nombre_dept);
when others then
    dbms_output.put_line('ERROR (sense definir)');

end;
/

begin
    department_a(&dept);
end;
/

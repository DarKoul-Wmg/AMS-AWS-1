set serveroutput on;

create or replace function comprovar_dept (ide departments.department_id%TYPE) return boolean
is
x numeric;
begin
    select department_id into x from departments where department_id = ide;
    return True;
    
exception
when no_data_found then
    return False;
end;
/

declare
begin
    if comprovar_dept(&dept) = True then
        dbms_output.put_line('EXISTEIX DEPARTAMENT');
    else
        dbms_output.put_line('NO EXISTEIX DEPARTAMENT');
    end if;
end;
/
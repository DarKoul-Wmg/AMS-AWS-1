set serveroutput on;

declare
    dept_id departments.department_id%type := &dept_id;
    dept_name departments.department_name%type := '&dept_name';
    
    dept_name_existe numeric;
    
    dept_existe exception;
    dept_n_existe exception;
begin
    select count(*) into dept_name_existe
    from departments where department_name = dept_name;
    
    if comprovar_dept(dept_id) then
        raise dept_existe;
    elsif dept_name_existe > 0 then
        raise dept_n_existe;
    else
        insert into departments (department_id, department_name) values (dept_id,dept_name);
        dbms_output.put_line('Operacion completada');
    end if;
    
exception
when dept_existe then
    dbms_output.put_line('ERROR: El id del departamento ya existe, porfavor, inserte uno nuevo');
when dept_n_existe then
    dbms_output.put_line('ERROR: El nombre del departamento ya existe, porfavor, inserte uno nuevo');
end;
/
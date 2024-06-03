set serveroutput on;

create or replace procedure Mostrarcaps (id_dept employees.department_id%type)
is
    cursor x is 
    select manager_id from employees where department_id = id_dept;
    
    nombre employees.first_name %type;
    departamento employees.department_id%type;
    
    nombre1 employees.first_name %type := 'xd';
    
    no_dept exception;
    exist_dept numeric;
    
    no_caps exception;
    non_caps numeric := 0;
begin
    select count(*) into exist_dept from departments where department_id = id_dept;
    if exist_dept = 0 then
        raise no_dept;
    end if;
    
    for i in x loop
        select first_name, department_id into nombre,departamento from employees where employee_id = i.manager_id;
        if departamento = id_dept then
            if nombre != nombre1 then
                dbms_output.put_line(nombre || ' es cap');
                nombre1 := nombre;
                non_caps := 1;
            end if;
        end if;
    end loop;
    if non_caps = 0 then
        raise no_caps;
    end if;
exception
when no_data_found then
    dbms_output.put_line('Steven es cap');
when no_dept then
    dbms_output.put_line('ERROR: No existeix el departament');
when no_caps then
    dbms_output.put_line('Aquest departament no te caps ');
when others then
    dbms_output.put_line('ERROR: Valor no valido');
end;
/

begin
    Mostrarcaps(&id);
end;
/
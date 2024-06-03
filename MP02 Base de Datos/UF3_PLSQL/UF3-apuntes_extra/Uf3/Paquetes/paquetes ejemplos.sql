set serveroutput on;

create or replace package ejemplo as

procedure dept_mostrar2(id departments.department_name%type);
function buscar_dept_nombre(id departments.department_name%type) return number;
end ejemplo;
/


create or replace package body ejemplo as



function buscar_dept_nombre(id departments.department_name%type) return number
as
v_num departments.department_id%type;
begin
select department_id into v_num from departments where department_name = id;
end buscar_dept_nombre;

procedure dept_mostrar2 (id departments.department_name%type)
is
    cursor x is
    select first_name from employees where department_id = 
    (select department_id from departments where department_name = id);
begin
    for i in x loop
        dbms_output.put_line(i.first_name);
    end loop;
end;
end ejemplo;
/


begin
    ejemplo.buscar_dept_nombre
end;
/



begin
    dept_mostrar('&dept');
end;

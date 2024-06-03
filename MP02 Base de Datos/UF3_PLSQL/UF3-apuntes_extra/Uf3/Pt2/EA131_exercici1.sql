set serveroutput on;

create or replace procedure imprimir_dades (ide employees.employee_id%TYPE)
is
    nombre employees.first_name%TYPE;
    salario employees.salary%TYPE;
    comision employees.commission_pct%TYPE;
    titulo jobs.job_title%TYPE;
    jefe_id employees.manager_id%TYPE;
    
    jefe employees.first_name%TYPE;
begin
    select e.first_name || ' ' || e.last_name as nom, e.salary, e.commission_pct, j.job_title, e.manager_id
    into nombre, salario, comision, titulo, jefe_id
    from employees e
    inner join jobs j on j.job_id=e.job_id
    where e.employee_id = ide;
    
    if jefe_id is null then
        jefe_id := ide;
    end if;
    if comision is null then
        comision := 0;
    end if;
    
    select first_name || ' ' || last_name as nom into jefe from employees where employee_id = jefe_id;
    
    dbms_output.put_line('Nombre: '|| nombre || chr(10)||'Oficio: '||titulo||chr(10)||'Salario: '||salario||chr(10)||'Comision: ' || comision||chr(10)||'Jefe: '||jefe);
exception
when no_data_found then
    dbms_output.put_line('No se ha encontrado al empleado');
end;
/

begin
    imprimir_dades(104);
end;
/
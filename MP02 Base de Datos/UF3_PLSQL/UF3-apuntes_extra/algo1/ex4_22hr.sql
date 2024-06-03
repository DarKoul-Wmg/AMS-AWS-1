set serveroutput on;

create or replace procedure forabecari (id_dept employees.department_id%type)
is
    cursor x is 
    select employee_id,first_name,last_name,email,phone_number,hire_date,job_id,salary,commission_pct,manager_id,department_id,(sysdate - hire_date)/365 as tiempo 
    from employees where department_id = id_dept order by tiempo asc fetch FIRST 2 rows only;

begin
    savepoint abc;
    
    for i in x loop
        insert into t_becaris_hist values (i.first_name,i.last_name,i.email,i.phone_number,i.hire_date,sysdate,i.job_id,i.salary,i.commission_pct,i.manager_id,i.department_id);
        
        delete from employees where employee_id = i.employee_id;
        dbms_output.put_line('Se ha eliminado correctamente a ' ||  i.first_name || ' ' || i.last_name);
    end loop;
exception
when no_data_found then
    dbms_output.put_line('No hay dos empleados en este departamento');
end;
/

begin
    forabecari(&id);
end;
/

rollback abc;

select * from employees where department_id = 10;


select * from t_becaris_hist;

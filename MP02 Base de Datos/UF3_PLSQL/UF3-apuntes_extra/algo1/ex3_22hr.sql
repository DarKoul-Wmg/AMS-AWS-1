set serveroutput on;

/*employee_id,first_name,last_name,email,phone_number,hire_date,job_id,salary,commission_pct,manager_id,department_id,*/

create or replace function old_emp (id_dept departments.department_id%type) return employees.employee_id%type
is
    cursor x is
    select employee_id, (sysdate - hire_date)/365 as tiempo from employees where department_id = id_dept order by tiempo desc fetch FIRST 1 rows only;
begin
    for i in x loop
        return i.employee_id;
    end loop;
end;
/

create or replace procedure dinoman
is
    cursor x is
    select department_id from employees group by department_id;
    
    id_emp employees.employee_id%type;
begin
    for i in x loop
        select old_emp(i.department_id) into id_emp from dual;
        dbms_output.put_line(id_emp);
    end loop;
end;
/

begin
    dinoman;
end;
/

select * from employees;

select old_emp(department_id) from employees group by department_id;

select department_id from employees group by department_id;

select * from departments;

set serveroutput on;

declare
    cursor ci is
    select employee_id,first_name,last_name,job_title
    from employees e
    inner join jobs j on j.job_id=e.job_id
    order by e.first_name
    fetch first 5 rows ONLY;
begin
    for i in ci loop
        dbms_output.put_line('Nombre: ' || i.first_name);
        dbms_output.put_line('E_ID: ' || i.employee_id);
    end loop;
    
end;
/

declare
    cursor ci is
    select employee_id,first_name,last_name,salary,job_title,email
    from employees e
    inner join jobs j on j.job_id=e.job_id
    order by e.first_name
    fetch first 5 rows ONLY;
    
    emp_row ci%rowtype;
begin
    open ci;
    loop
        fetch ci into emp_row;
        
        exit when ci%notfound;
        --exit when emp_row.employee_id = 196;
        dbms_output.put_line('Nombre: ' || emp_row.first_name);
        dbms_output.put_line('E_ID: ' || emp_row.employee_id);
        
    end loop;
    close ci;
end;
/
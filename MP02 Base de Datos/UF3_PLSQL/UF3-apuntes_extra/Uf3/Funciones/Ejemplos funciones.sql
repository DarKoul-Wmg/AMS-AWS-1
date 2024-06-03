create or replace NONEDITIONABLE function ex1 (num1 numeric, num2 numeric) return number
is
begin
    if num1 > num2 then
        return num1;
    elsif num1 < num2 then
        return num2;
    else
        return num1;
    end if;
end;
/

select ex1(2,1) from dual;

create or replace NONEDITIONABLE function ex2 (num1 numeric, num2 numeric) return boolean
is
begin
    if mod(num1,num2) = 0 then
        return True;
    else
        return False;
    end if;
end;
/

declare
    a boolean;
begin
    a := ex2(1,5);
    if a = True then
        dbms_output.put_line('True');
    elsif a = False then
        dbms_output.put_line('False');
    end if;
end;
/

create or replace function employee_pasw (id_employee employees.employee_id%TYPE) return varchar2
is
    existe numeric;
    pasword varchar2(20);
begin
    select count(*) into existe from employees where employee_id = id_employee;
    if existe = 0 then
        return 'El empleado no existe';
    else
        select upper(substr(first_name,1,2))||lower(substr(last_name,-1))||employee_id*3||department_id||'@' 
        into pasword
        from employees where employee_id=id_employee;
        
        return pasword;
    end if;
    
end;
/

select employee_pasw(employee_id) from employees;
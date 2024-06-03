declare
v_id employees.employee_id%TYPE;
v_first_name employees.first_name%type;
v_last_name employees.last_name%type;
BEGIN
FOR v_id IN 100..140 LOOP
    select first_name,last_name into v_first_name,v_last_name  
    from employees where department_id=v_id;
    DBMS_OUTPUT.PUT_LINE('El nom del treballador:'||v_id||' és '|| v_first_name||', '||v_last_name);
END LOOP;
end;

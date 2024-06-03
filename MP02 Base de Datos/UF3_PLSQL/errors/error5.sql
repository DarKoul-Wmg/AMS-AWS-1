declare
v_id number:=0;
v_count number:=0;
BEGIN
    v_id=90;
    select count(*) into v_count  
    from employees where department_id=v_id;
    DBMS_OUTPUT.PUT_LINE('El total de treballadors de :'||v_id||' és '|| v_count);
END;

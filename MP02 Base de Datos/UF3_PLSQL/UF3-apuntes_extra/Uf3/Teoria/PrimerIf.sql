SET SERVEROUTPUT ON;

DECLARE
    id employees.employee_id%TYPE;
    estado locations.state_province%TYPE;
    name employees.first_name%TYPE;
BEGIN
    id := &id;
    select state_province, first_name
    into estado, name
    from employees e 
    inner join departments d on d.department_id=e.department_id
    inner join locations l on l.location_id=d.location_id
    where e.employee_id = id;
    IF estado = 'Texas' THEN
        DBMS_OUTPUT.PUT_LINE('El trabajador ' || name || 'trabaja en Texas.');
    ELSE
        DBMS_OUTPUT.PUT_LINE('El trabajador no trabaja en Texas.');
    END IF;
END;
/


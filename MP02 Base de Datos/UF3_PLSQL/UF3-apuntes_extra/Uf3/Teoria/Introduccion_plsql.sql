/*Ex1*/
DECLARE
    name departments.department_name%TYPE;
BEGIN
    select department_name
    into name
    from departments
    where department_id = (select department_id from employees where employees.first_name = 'Pat');
    DBMS_OUTPUT.PUT_LINE('EL nombre del departamento es: ' || name);
END;
/

/*Ex2*/
DECLARE
    id number;
    name regions.region_name%TYPE;
BEGIN
    id := &id;
    select r.region_name
    into name
    from employees e
    inner join departments d on d.department_id=e.department_id
    inner join locations l on l.location_id=d.location_id
    inner join countries c on c.country_id=l.country_id
    inner join regions r on r.region_id=c.region_id
    where e.employee_id = id
    ;
    DBMS_OUTPUT.PUT_LINE('La region de trabajador es: ' || name);
END;
/

/*Ex3*/

SET SERVEROUTPUT ON;
DECLARE
    variable varchar2(100);

BEGIN
    variable := 'HOLA MUNDO';
    DBMS_OUTPUT.PUT_LINE(variable);
    variable := 'FIN DEL PROGRAMA';
    DBMS_OUTPUT.PUT_LINE(variable);
END;
/

/*Ex4*/
DECLARE
    var1 number;
    var2 number;
BEGIN
    var1 := 10.2;
    var2 := 20.1;
    DBMS_OUTPUT.PUT_LINE((var1 + var2));
END;
/

/*Ex5*/
DECLARE
    var1 employees.first_name%TYPE;
BEGIN
    select upper(first_name) into var1 from employees where employee_id=&id;
    DBMS_OUTPUT.PUT_LINE('El name es: ' || var1);
END;
/

/*Ex6*/
DECLARE
    Percentage CONSTANT NUMBER := 0.10;
    row employees%ROWTYPE;
    id number;
    departamento departments.department_name%TYPE;
    
BEGIN
    id := &id;
    select e.first_name, e.last_name, d.department_name, e.salary
    into row.first_name, row.last_name, departamento, row.salary
    from employees e
    inner join departments d on d.department_id=e.department_id
    where e.employee_id = id;
    
    DBMS_OUTPUT.PUT_LINE('EL usuario con id: ' || id );
    DBMS_OUTPUT.PUT_LINE('El usuario con el Nombre: ' || row.first_name || ' y con el apellido ' || row.last_name || ' que pertenece al departamento ' || departamento);
    DBMS_OUTPUT.PUT_LINE('El salario inicial era: ' || row.salary || ' y ahora el nuevo salario es ' || ((1+Percentage)*row.salary));
END;
/
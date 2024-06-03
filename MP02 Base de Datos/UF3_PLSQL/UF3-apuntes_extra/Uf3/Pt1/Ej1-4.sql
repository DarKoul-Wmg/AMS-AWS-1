SET SERVEROUTPUT ON;
/*Ex1*/

DECLARE
    ID_DEPT DEPARTMENTS.DEPARTMENT_ID%TYPE;
    NOMBRE DEPARTMENTS.DEPARTMENT_NAME%TYPE;
    MEDIA EMPLOYEES.SALARY%TYPE;
    EXISTE NUMERIC;
BEGIN
    ID_DEPT := &ID_DEPT;
    SELECT COUNT(*) INTO EXISTE FROM EMPLOYEES WHERE DEPARTMENT_ID = ID_DEPT;
    IF EXISTE >= 1 THEN
        SELECT AVG(SALARY), D.DEPARTMENT_NAME
        INTO MEDIA, NOMBRE
        FROM EMPLOYEES E
        INNER JOIN DEPARTMENTS D ON E.DEPARTMENT_ID=D.DEPARTMENT_ID
        WHERE D.DEPARTMENT_ID = ID_DEPT
        GROUP BY d.department_name;
        DBMS_OUTPUT.PUT_LINE(ID_DEPT || ' - ' || NOMBRE || ' - El salario medio de este departamento es de ' || TRUNC(MEDIA));
        
    ELSE
        DBMS_OUTPUT.PUT_LINE('El departamento no existe');
    END IF;
END;
/

/*Ex2*/

Create table EMPLOYEES_NEW_SALARY (
emp_id numeric,
dept_id numeric,
new_salary numeric
);
END;


DECLARE
    ID_DEPT DEPARTMENTS.DEPARTMENT_ID%TYPE;
    NOMBRE DEPARTMENTS.DEPARTMENT_NAME%TYPE;
    MEDIA EMPLOYEES.SALARY%TYPE;
    EXISTE NUMERIC;
    
BEGIN
    ID_DEPT := &ID_DEPT;
    SELECT COUNT(*) INTO EXISTE FROM EMPLOYEES WHERE DEPARTMENT_ID = ID_DEPT;
    IF EXISTE >= 1 THEN
        SELECT AVG(SALARY), D.DEPARTMENT_NAME
        INTO MEDIA, NOMBRE
        FROM EMPLOYEES E
        INNER JOIN DEPARTMENTS D ON E.DEPARTMENT_ID=D.DEPARTMENT_ID
        WHERE D.DEPARTMENT_ID = ID_DEPT
        GROUP BY d.department_name;
        DBMS_OUTPUT.PUT_LINE(ID_DEPT || ' - ' || NOMBRE || ' - El salario medio de este departamento es de ' || TRUNC(MEDIA));
        if media < 6000 then
            insert into EMPLOYEES_NEW_SALARY select employee_id, department_id, (salary*1.30) from employees where department_id = ID_DEPT;
        end if;
    ELSE
        DBMS_OUTPUT.PUT_LINE('El departamento no existe');
    END IF;
end;
/

/*Ex3*/

declare
    id_dept employees.department_id%type;
    existe numeric;
    num_empl numeric;
    sueldo_min employees.salary%type;
    sueldo_max employees.salary%type;
    fecha date;
    salario numeric;
    email departments.department_name%type;
    
begin
    id_dept := &id_dept;
    
    SELECT COUNT(*) INTO existe FROM EMPLOYEES WHERE DEPARTMENT_ID = id_dept;
    
    if existe > 0 then
        select count(employee_id) into num_empl from employees where department_id = id_dept;
        
        if num_empl < 10 then
            
            select min(salary), max(salary)
            into sueldo_min, sueldo_max
            from employees
            where department_id = id_dept;
            
            select department_name
            into email
            from departments
            where department_id = id_dept;

            dbms_output.put_line('El departamento ' || id_dept || ' tiene ' || num_empl || '. Necesitamos ' || (10-num_empl) || ' más.');
            SELECT sysdate into fecha from dual;
            
            for i in num_empl+1..10 loop
                
                salario := trunc(dbms_random.value((sueldo_min-500),(sueldo_max+4000)));
                dbms_output.put_line('Tabajador'||i|| ' contratado el '|| fecha ||' con un salario de ' || salario);
                insert into employees (employee_id,first_name, last_name,email, hire_date,job_id, salary, department_id) 
                    values ( (select max(employee_id +1) from employees),
                    'Trabajador',
                    i,
                    email||i,
                    fecha,
                    (select max(job_id) from employees where department_id = id_dept),
                    salario,
                    id_dept);
                
                fecha := fecha + 7;
                
            end loop;
            dbms_output.put_line('¡El departamento ya tiene a todos sus empleados!');
            
        else
            dbms_output.put_line('No es necesario contratar a nadie');
            
        end if;
        
    else
        dbms_output.put_line('Este departamento no existe');
        
    end if;
end;
/


/*Ex4*/


declare
    nombre_pok pok_pokemon.nombre%type;
    existe numeric;
    numero_hab numeric;
    nombre_mov pok_movimiento.nombre%type;
    tipo_mov pok_tipo.nombre%type;
begin
    nombre_pok := '&nombre_pok';
    select upper(SUBSTR(nombre_pok, 1, 1)) || lower(substr(nombre_pok , 2)) into nombre_pok from dual;
    
    select count(*) into existe from pok_pokemon where nombre = nombre_pok;
    
    if existe >= 1 then
        numero_hab := &numero_hab;
        
        if numero_hab <= 0 then
            dbms_output.put_line('El pokemon ' || nombre_pok || ' existe y has decidido mostrar 0 movimientos. ');
            
        else
            
            dbms_output.put_line('El pokemon ' || nombre_pok || ' existe y estos son todos sus movimientos:');
        
            for i in 1 .. numero_hab loop
                select NOMMOV, TIPO 
                into nombre_mov, tipo_mov
                from
                    (select nom,nommov,tipo, rownum as r from
                    (select pok.nombre as nom,mov.nombre as nommov,pok_tipo.nombre aS TIPO from pok_pokemon pok
                    inner join pok_pokemon_movimiento_forma pok_mov on pok_mov.numero_pokedex = pok.numero_pokedex
                    inner join pok_movimiento mov on pok_mov.id_movimiento = mov.id_movimiento
                    inner join pok_tipo on pok_tipo.id_tipo = mov.id_tipo
                    where pok.nombre = nombre_pok)
                    )where r = i;
                dbms_output.put_line(nombre_mov || ' de tipo ' || tipo_mov);
                
            end loop;
        end if;
    else
        dbms_output.put_line('El pokemon ' || nombre_pok || ' no existe.');
        
    end if;
end;
/
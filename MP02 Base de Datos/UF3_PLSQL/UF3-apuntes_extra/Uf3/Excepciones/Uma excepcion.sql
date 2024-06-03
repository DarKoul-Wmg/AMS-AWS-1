set serveroutput on;

declare
    numero numeric;
    nom cliente.nombre_cliente%type;
begin
    select nombre_cliente into nom from cliente where codigo_cliente = &numero;
        dbms_output.put_line('Nom: ' || nom);
    EXCEPTION
    when no_data_found then
        dbms_output.put_line('No data found');
end;
/



declare
    emp_id number;
    comi employees.commission_pct%type;
    no_com exception;
begin

    emp_id := &emp_id;
    
    select employee_id,commission_pct into emp_id , comi from employees where employee_id = emp_id;
    
    if (comi is null) then
        raise no_com;
    end if;
    dbms_output.put_line(emp_id);
    
commit;
exception
when no_data_found then
    dbms_output.put_line('No hay nada por pete');
    ROLLBACK;
when too_many_rows then
    dbms_output.put_line('Muchas rows pete');
    ROLLBACK;
when no_com then
    dbms_output.put_line('Comision nula');
    ROLLBACK;
    
when OTHERS then
    dbms_output.put_line('Nu se');
    ROLLBACK;
end;
/

set serveroutput on;

declare
    ide jobs.job_id%type := '&ide';
    tit jobs.job_title%type := '&tit';
    mins jobs.min_salary%type := '&mins';
    maxs jobs.max_salary%type := '&maxs';
    
    vacio exception;
    minimo_mayor exception;
    sueldo_0 exception;
    mala_length exception;
begin
    if (ide is null) or (tit is null) or (mins is null) or (maxs is null) then
        raise vacio;
    elsif mins > maxs then
        raise minimo_mayor;
    elsif mins < 0 or maxs < 0 then
        raise sueldo_0;
    elsif length(ide) not between 5 and 10 or length(tit) not between 5 and 10 then
        raise mala_length;
    end if;
    
    insert into jobs values (ide, tit, mins, maxs);
    commit;
    
    exception
    when dup_val_on_index then
        dbms_output.put_line('Estas intentando agregar valores duplicados');
        rollback;
    when vacio then
        dbms_output.put_line('No puedes insertar valores vacios');
        rollback;
    when minimo_mayor then
        dbms_output.put_line('El sueldo minimo no puede ser mayor al maximo');
        rollback;
    when mala_length then
        dbms_output.put_line('La id y el titulo han de estar entre 5 y 10 caracteres');
        rollback;
    when sueldo_0 then
        dbms_output.put_line('Los sueldo no pueden ser menores que 0');
        rollback;
end;
/

select * from jobs;
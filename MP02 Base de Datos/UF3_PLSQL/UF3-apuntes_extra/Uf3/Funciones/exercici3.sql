set SERVEROUTPUT on;

create or replace procedure dar_alta_oficio (id jobs.job_id%type, title jobs.job_title%type, minim jobs.min_salary%type, maxim jobs.max_salary%type)
IS
    existeid numeric;
    existejob numeric;
begin
    select count(*) into existeid from jobs where job_id = 'id';
    select count(*) into existejob from jobs where job_title = 'title';
    if existeid != 0 or existejob != 0 then
        dbms_output.put_line('Este id o titulo ya existen');
    elsif minim > maxim then
        dbms_output.put_line('El salario maximo a de ser mayor al minimo');
    elsif minim < 0 or maxim < 0 then
        dbms_output.put_line('El salario maximo o minimo a de ser superior o igual a 0');
    else
        insert into jobs values (id, title, minim, maxim);
        dbms_output.put_line('El trabajo ' || title || ' de id ' || id || ' se ha agregado correctamente.');
    end if;
end;
/

BEGIN
    dar_alta_oficio('&ide','&titulo',&minimo,&maximo);
end;
/
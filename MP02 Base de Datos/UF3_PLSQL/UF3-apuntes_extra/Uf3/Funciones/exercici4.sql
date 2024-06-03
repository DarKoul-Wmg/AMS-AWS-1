create or replace procedure dar_baja_oficio (ide jobs.job_id%type)
IS
    existeid numeric;
begin
    select count(*) into existeid from jobs where job_id = ide;
    if existeid != 0 then
        delete from jobs where job_id = ide; 
        dbms_output.put_line('El trabajo eliminado correctamente.');
    else
        dbms_output.put_line('Este id no existe');
    end if;
end;
/
begin
    dar_baja_oficio('&ide');
end;
/
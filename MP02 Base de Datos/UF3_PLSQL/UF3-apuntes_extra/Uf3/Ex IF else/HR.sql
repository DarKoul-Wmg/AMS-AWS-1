set serveroutput on;

declare
    id jobs.job_id%TYPE;
    tittle jobs.job_title%type;
    minsalary jobs.min_salary%type;
    maxsalary jobs.max_salary%type;
    
    job_id jobs.job_id%TYPE;
    job_id_c numeric;
    
    job_title jobs.job_title%type;
    job_tittle_c numeric;
begin
    id := &id;
    tittle := &tittle;
     minsalary := &minsalary;
     maxsalary := &maxsalary;
    select count(job_id) into job_id_c from jobs where job_id = id;
    select count(job_title) into job_tittle_c from jobs where job_title = tittle;
    if job_id_c > 0 then
        dbms_output.put_line('Coloca una ID que no este repetida');
    elsif not length(id) between 5 and 10 then
        dbms_output.put_line('La longitud de Job ID es incorrecta');
    elsif job_tittle_c > 0 then
        dbms_output.put_line('Coloca un titulo que no este repetido');
    elsif not length(tittle) between 5 and 35 then
        dbms_output.put_line('La longitud de titulo es incorrecto');
    elsif minsalary < 0 then
        dbms_output.put_line('El salario minimo no puede ser negativo');
    elsif maxsalary < 0 then
        dbms_output.put_line('El salario maximo no puede ser negativo');
    elsif minsalary > maxsalary then
        dbms_output.put_line('El salario minimo no puede ser mayor al salario maximo');
    else
        insert into jobs values (id, tittle, minsalary, maxsalary);
        dbms_output.put_line('Se ha añadido correctamente');
    end if;
end;
/

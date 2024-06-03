create or replace function contar (dep_num departments.department_id%TYPE) return number
is
    numero numeric;
begin
    select count(*) into numero from employees
    where department_id = dep_num;
    if numero != 0 then
        return numero;
    else
        return null;
    end if;
end;
/
select contar(&id_dep) from dual;

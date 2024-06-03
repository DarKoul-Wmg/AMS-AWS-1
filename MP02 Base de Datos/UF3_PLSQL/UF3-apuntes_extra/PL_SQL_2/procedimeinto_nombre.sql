SET SERVEROUTPUT ON;

create or replace PROCEDURE obtener_nombre(numid in number,nom in out employees.first_name%TYPE, ape in out employees.last_name%TYPE )
is 
existe number;

begin
select count(*) into existe from employees where employee_id=numid;

if existe=1 then
select first_name,last_name into nom , ape  from employees where employee_id =numid;

else
nom:='no existe';
ape:='no existe';

end if;
end obtener_nombre;
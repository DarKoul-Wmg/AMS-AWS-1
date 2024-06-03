SET SERVEROUTPUT ON

/*
Realitza un procediment anomenat "Mostrarcaps" que rebi el número d'un department 
i mostri el nom dels empleats d'aquest department que són caps d'altres empleats. 
Tracta les excepcions que consideris oportunes i crea una excepció que controle 
exclusivament que controli que existeix el departament. Realitza el bloc anònim 
corresponent per cridar al procediment.
*/
select DEPARTMENT_ID, manager_id from departments;
select DEPARTMENT_ID, manager_id from departments ;


create or replace PROCEDURE Mostrarcaps(id_depa in out departments.departmen_id%type, id_ma in out departments.manager_id%type )
is 

begin

if manager_id is not null then
    select  department_id into id_depa, manager_id into id_ma from departments ;
end if;
end Mostrarcaps;


Declare
id_depa departments.departmen_id%type;
id_ma departments.manager_id%type;
begin 
mostrarcaps(10,200);
dbms_output.put_line(id_depa|| ' ' || id_ma);
end;


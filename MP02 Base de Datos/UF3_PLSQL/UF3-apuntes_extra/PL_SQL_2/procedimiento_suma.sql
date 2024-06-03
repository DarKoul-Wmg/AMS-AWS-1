SET SERVEROUTPUT ON;

create or replace PROCEDURE suma(num1 number, num2 number, suma in out number)
is 
begin
if (num1 > 0 or num2 > 0 ) then
suma:=(num1+num2);
dbms_output.put_line(suma );
end if;
end suma;
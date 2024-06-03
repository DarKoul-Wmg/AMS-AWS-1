SET SERVEROUTPUT ON;
declare
numsum number;
begin
suma(&var1,&var2,numsum);
dbms_output.put_line('la var sum es ' || suma );
end;

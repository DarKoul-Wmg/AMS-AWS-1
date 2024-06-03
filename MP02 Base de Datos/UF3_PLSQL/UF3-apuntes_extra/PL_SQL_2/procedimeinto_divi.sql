-- dividir un numero que se pase como parametros
create or replace NONEDITIONABLE PROCEDURE DividirNumero(dividento in number ,divisor in number, cociente out number,resto out number)
is 
begin 
if (divisor>0) then
cociente:= trunc(dividento/divisor);
resto:= mod(dividento,divisor);
dbms_output.put_line('dividendo' || dividento );
dbms_output.put_line('divisor' ||divisor  );
dbms_output.put_line('cociente' || cociente );
dbms_output.put_line('resto' || resto );
end if;
end DividirNumero;
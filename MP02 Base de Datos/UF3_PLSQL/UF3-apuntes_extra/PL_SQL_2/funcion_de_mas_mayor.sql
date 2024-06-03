create or replace FUNCTION  mayor(a  number, b  number)
RETURN number 
is
maximo number;
begin
if (a >= b)
    then 
        maximo:=a;
    else
        maximo:=b;
end if;
RETURN  maximo ; --- ponemos lo de la funcion
end;
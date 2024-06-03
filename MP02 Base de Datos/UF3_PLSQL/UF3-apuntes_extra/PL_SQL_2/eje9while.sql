SET SERVEROUTPUT ON;
/* Programar un script que en nos enseñe los numeros entre un rango  con fo y while minim = 1 max input  */

DECLARE
i NUMBER:=0;
maximo INT; 

BEGIN
maximo := &maximo;

if maximo <=0 then
DBMS_OUTPUT.PUT_LINE('Error');
else;
WHILE i <= maximo LOOP
    DBMS_OUTPUT.PUT_LINE('El numero es: '|| i);
    i:=i+1;
    END LOOP;
END;
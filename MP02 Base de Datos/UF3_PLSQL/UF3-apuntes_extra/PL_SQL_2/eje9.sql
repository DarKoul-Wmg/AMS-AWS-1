SET SERVEROUTPUT ON;
/* Programar un script que en nos enseñe los numeros entre un rango  con fo y while minim = 1 max input  */


DECLARE

maxi INT; 

BEGIN
maxi := &maxi;

for i in 1..maxi LOOP
    DBMS_OUTPUT.PUT_LINE('El numero es: '|| i);
    END LOOP;
END;



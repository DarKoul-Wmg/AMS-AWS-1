SET SERVEROUTPUT ON;
/* Programa que muestre los numeros con un rango de salto  
    if nim >  max  error
    if salto < 0 error 
    while (nim< max)
    nim = nim + salto
    
*/

DECLARE

minimo INT;
maximo INT; 
salto INT;

BEGIN
minimo:=&minimo;
maximo:=&maximo;
salto:=&salto;

IF salto < 1 THEN
        DBMS_OUTPUT.PUT_LINE('El numero es de salto es menor que 0');

ELSIF minimo > maximo THEN
        DBMS_OUTPUT.PUT_LINE('Error');   

ELSE
    while minimo < maximo LOOP    
    DBMS_OUTPUT.PUT_LINE('El numero es ' || minimo || ' El numero de salto es ' || salto );    
    minimo:= minimo + salto;
END LOOP; 
END IF;
END;
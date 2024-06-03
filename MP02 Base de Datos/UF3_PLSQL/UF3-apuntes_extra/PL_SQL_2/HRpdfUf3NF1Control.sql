SET SERVEROUTPUT ON;
--- PDF Exercicios ---
--- Eje 4 ---

DECLARE

salario INT; 

BEGIN
salario := &salario;

    IF salario < 100 then
    DBMS_OUTPUT.PUT_LINE('La comision es de 10%: ' ||(salario*10)/100);
    ELSIF salario BETWEEN '100' AND '500' then
    DBMS_OUTPUT.PUT_LINE('La comision es de 15% ' ||(salario*15)/150);
    ELSIF salario >1000 then
    DBMS_OUTPUT.PUT_LINE('La comision es de 20% ' ||(salario*20)/200);
    END IF;
END;

--- Eje 5 ---

DECLARE

EDAD INT; 

BEGIN
EDAD := &EDAD;

    IF EDAD < 18 then
    DBMS_OUTPUT.PUT_LINE('Eres menor de edad ' );
    ELSIF EDAD = 18 then
    DBMS_OUTPUT.PUT_LINE('Casi eres mayor de edad ' );
    ELSIF EDAD > 18 then
    DBMS_OUTPUT.PUT_LINE('Eres mayor de edad ' );
    ELSIF EDAD < 40 then
    DBMS_OUTPUT.PUT_LINE('Eres Juvenil' );
    ELSIF EDAD < 0 then
    DBMS_OUTPUT.PUT_LINE('Error de edad no puede ser negativo  ' );
    
    END IF;
END;

--- Eje 6 ---

DECLARE

numero INT;

BEGIN
numero := &numero;
    
    DBMS_OUTPUT.PUT_LINE(' La suma de numero +4 = '|| numero + 4 );
    DBMS_OUTPUT.PUT_LINE(' La resta de numero - 3 es =  '|| numero - 3 );
    DBMS_OUTPUT.PUT_LINE(' La multiplicaccio de numero * 8 es =  '|| numero * 8 );
END;



---No lo entiendo ---
--- Eje 7 ---
DECLARE 

num1 INT;
num2 INT;

BEGIN
num1 :=&num1;
num2 :=&num2;
IF num1 <0 or num2 < 0 then
DBMS_OUTPUT.PUT_LINE('No es un numero positivo ');

ELSIF num1 >0 or num2 >0 then
DBMS_OUTPUT.PUT_LINE('La suma de los numeros son'||(num1 + num2) /num2 );
END IF;
END;

---No lo entiendo ---
--- Eje 8 ---
DECLARE 

num1 INT;
num2 INT;

BEGIN
num1 :=&num1;
num2 :=&num2;
IF num1 <0 or num2 < 0 then
DBMS_OUTPUT.PUT_LINE('No es un numero positivo ');
ELSIF num1 > num2 then
DBMS_OUTPUT.PUT_LINE('El primer numero tiene que ser mas grande');
ELSIF num1 >0 or num2 >0 then
DBMS_OUTPUT.PUT_LINE('La suma de los numeros son'||(num1 + num2) /num2 );
END IF;
END;





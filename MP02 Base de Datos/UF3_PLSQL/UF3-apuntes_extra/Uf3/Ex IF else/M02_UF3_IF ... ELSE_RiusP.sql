set serveroutput on;

/*Ex4*/
declare
numero numeric;
begin
numero := &numero;
if numero < 100 then
dbms_output.put_line('Tu comision es de ' || (numero*0.1));
elsif numero between 100 and 500 then
dbms_output.put_line('Tu comision es de ' || (numero*0.15));
elsif numero > 1000 then
dbms_output.put_line('Tu comision es de ' || (numero*0.2));
end if;
end;
/

/*Ex5*/
declare
    edad numeric;
begin
    edad := &edad;
    if edad < 0 then
        dbms_output.put_line('Error edad no puede ser negativo');
    elsif edad > 40 then
        dbms_output.put_line('Eres viejoven');
    elsif edad < 18 then
        dbms_output.put_line('Eres menor de edad');
    elsif edad = 18 then
        dbms_output.put_line('Eres casi mayor de edad');
    elsif edad > 18 then
        dbms_output.put_line('Eres mayor de edad');
    end if;
end;
/

/*Ex6*/
declare
    numero constant numeric := &numero;
    suma numeric := 4 + numero;
    resta numeric := numero - 3;
    multi numeric := numero * 8;
begin
    dbms_output.put_line('Suma: ' || suma || ' Resta: ' || resta || ' Multiplicacion: ' || multi);
end;
/

/*Ex7*/
declare
    num1 numeric;
    num2 numeric;
    resultado numeric;
begin
    num1 := &num1;
    num2 := &num2;
    resultado := ((num1/num2)+num2);
    if num1 < 0 or num2 < 0 then
        dbms_output.put_line('Inserta numero positivos');
    else
        dbms_output.put_line('Resultado: ' || resultado);
    end if;
end;
/

/*Ex8*/
declare
    num1 numeric;
    num2 numeric;
    resultado numeric;
begin
    num1 := &num1;
    num2 := &num2;
    resultado := ((num1/num2)+num2);
    if num1 < 0 or num2 < 0 then
        dbms_output.put_line('Inserta numero positivos');
    elsif num1 < num2 then
        dbms_output.put_line('Error! el primer numero tiene que ser má
        s grande que el segundo');
    else
        dbms_output.put_line('Resultado: ' || resultado);
    end if;
end;
/
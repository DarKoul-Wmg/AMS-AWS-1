set serveroutput on;

declare
 numsum numeric;

begin
    suma(&var1, &var2 , numsum);
    dbms_output.put_line('La var sum es ' || numsum);
end;
/


declare
    nombre employees.first_name%type;
    apellido employees.last_name%type;
begin
    dbms_output.put_line('Nombre vacio: ' || nombre || ' ' || apellido);
    obtener_nombre(100,nombre,apellido);
    dbms_output.put_line('Nombre: ' || nombre || ' ' || apellido);
end;
/

/*Ex1 PDF*/
begin
    listarNumeros(&numero);
end;
/

/*Ex2 PDF*/
declare
    num1 numeric;
    num2 numeric;
    
    cociente numeric;
    residuo numeric;
begin
    DividirNumeros(&num1,&num2,cociente,residuo);
end;
/

/*Ex1 MAS EJ PDF*/
begin
    ex1MasEx(&num);
end;
/

/*Ex2 MAS EJ PDF*/
begin
    duplicar_cantidad(&num);
end;
/

select * from jobs;
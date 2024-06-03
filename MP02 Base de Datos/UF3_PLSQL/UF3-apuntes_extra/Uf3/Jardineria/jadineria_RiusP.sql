set serveroutput on;

/*Ex1*/
create or replace function DelReves (cadena producto.codigo_producto%TYPE) return varchar2
is
    reverso varchar2(32767);
begin
    select reverse(cadena) into reverso from dual;
    return reverso;
end;
/

select codigo_producto, DelReves(codigo_producto) from producto;

/*Ex2*/
create or replace function DifDias (ped pedido.codigo_pedido%TYPE) return number
is
    diferencia number;
    comprovante pedido.fecha_entrega%TYPE;
begin
    select fecha_entrega into comprovante from pedido where codigo_pedido = ped;
    if comprovante is null then
        return null;
    else
        select (fecha_entrega - fecha_pedido) into diferencia from pedido where codigo_pedido = ped;
        return diferencia;
    end if;
end;
/

select DifDias(codigo_pedido) from pedido;

/*Ex3*/

create or replace procedure apellidos_y_limite 
is
    ape cliente.apellido_contacto%type;
    lim cliente.limite_credito%type;
    cod cliente.codigo_cliente%type;
begin
    for i in 1..5 loop
        select codigo_cliente into cod from(
        select rownum as r, codigo_cliente from (
        select codigo_cliente
        from pago
        group by codigo_cliente 
        order by sum(total) desc))
        where r = i;
        
        select apellido_contacto, limite_credito into ape, lim from cliente where codigo_cliente = cod;
        dbms_output.put_line('Apellido: ' || ape || ' - ' || 'Limite: ' || lim);
    end loop;
end;
/

begin
    apellidos_y_limite;
end;
/

/*Ex4*/
create or replace procedure exec_pagos (ide cliente.codigo_cliente%type)
is
    existe numeric;
    nom cliente.nombre_cliente%type;
    ciu cliente.ciudad%type;
    pai cliente.pais%type;
    total numeric;
begin
    select count(*) into existe from cliente where codigo_cliente = ide;
    if existe = 0 then
        dbms_output.put_line('Este cliente no existe');
    else
        select nombre_cliente, ciudad, pais into nom, ciu, pai from cliente where codigo_cliente = ide;
        select sum(total) into total from pago where codigo_cliente = ide;
        dbms_output.put_line('CODIGO CLIENTE: ' || ide || chr(10) || 'NOMBRE CLIENTE: ' || nom || chr(10) || 'CIUDAD CLIENTE: ' || ciu || chr(10) || 'PAIS CLIENTE: ' || pai
                             || chr(10) ||  'TOTAL PAGOS EFECTUADOS: ' || total);
    end if;
end;
/
begin
    exec_pagos(1);
end;
/

/*Ex5*/
create or replace function factorial (numero numeric) return numeric
is
    num numeric;
begin
    num := 1;
    for i in reverse 1..numero loop
        num := num * i;
    end loop;
    return num;
end;
/

select factorial(6) from dual;
/* que muestre todos los codigos de los usuarios  */ 
SET SERVEROUTPUT ON;

create or replace PROCEDURE productos(codi in out producto.codigo_producto%TYPE)
is 
existe number;

begin
select count(*) into existe from producto where codigo_producto=codi;

if existe=1 then
select reverse(codigo_producto) into codi from producto  where codigo_producto=codi;
end if;
end productos;
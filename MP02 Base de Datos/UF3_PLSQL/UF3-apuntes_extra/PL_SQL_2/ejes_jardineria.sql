Set SERVEROUTPUT on;
/* Práctica 2 parte 1 Sobre BBDD Jardineria */

/* 1- Realizar una función llamada DelReves que a partir de un codig
de producto, nos devuelva el código de producto al revés.
Utilizar en una consulta de ejemplo para comprobar que funciona.

*/
select codigo from producto;

create or replace function delReves(j_id  producto.codigo_producto %TYPE) return varchar 
is 
cod varchar(50);
begin
select reverse(codigo_producto) into cod from producto where codigo_producto= j_id;

return cod;
end;


/*
2- Desarrolla una función llamada DifDias que devuelva la diferencia de días
entre la fecha de pedido y la fecha de entrega
para un pedido introducido por el usuario.
*/

select * from pedido;
select fecha_pedido,fecha_entrega from pedido;

create or replace FUNCTION DifDias( pedido pedido.fecha_pedido%TYPE, entrega pedido.fecha_entrega%type) retunr date 


/*
3- Escribir un procedimiento almacenado que visualice el apellido 
y el limite de credito de los cinco clientes que más
dinero se han gastado.1
*/
create or replace procedure mostrar
is 
id_cli jardineria_cliente.codigo_cliente%type;
apell jardineria_cliente.apellido_contacto%type;
limite jardineria_cliente.limite_creditos%type;
begin fro i in 1 .. 5
loop


select codigo_cliente from
(
select codigo_cliente,tot,rownum as r from
(select  codigo_cliente, sum(total) as tot from jardineria_pago
group by codigo_cliente order by sum(total)desc 
)
)
where r=i;

select apellido_contacto,limite_credito into apell,limit from jardineria_cliente where codigo_cliente=id_cli;

DBMS_OUTPUT.PUT_LINE('apell|| ' '|| limite);

end loop;
end; 




/*

4- Procedimiento almacenado que al pasarle un codigo de cliente, nos liste lo siguiente
( en el mismo formato que la imagen )
- Código cliente, nombre, ciudad, pais
- Cantidad total pagada.
Omitir los pagos realizados.

*/



/*
5 - Programar una función que calcule el factorial de un numeroq ue se le pase
como parametro. La función se llamará factorial.
*/
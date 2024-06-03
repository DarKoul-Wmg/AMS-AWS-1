set SERVEROUTPUT on;

/*Ex1*/

create or replace procedure aumenta_pecio (editori libros.editorial%TYPE)
is
    existe numeric;
begin
    select count(*) into existe from libros where editorial = editori;
    if existe = 0 then
        dbms_output.put_line('Esta editorial no existe');
    else
        update libros
        set precio = (precio * 1.10)
        where editorial = editori;
        dbms_output.put_line('El precio se ha actualizado');
    end if;
end;
/

begin
    aumenta_pecio('&nombre');
end;
/
/*Ex2*/

create or replace procedure aumenta_pecio_mas (editori libros.editorial%TYPE, aumento numeric default 10)
is
    existe numeric;
begin
    select count(*) into existe from libros where editorial = editori;
    if existe = 0 then
        dbms_output.put_line('Esta editorial no existe');
    else
        update libros
        set precio = (precio * (1 + (aumento/100)))
        where editorial = editori;
        dbms_output.put_line('El precio se ha actualizado');
    end if;
end;
/

begin
    aumenta_pecio_mas('&nombre',&au);
end;
/

create or replace PROCEDURE add_libros (title libros.titulo%type, author libros.autor%type, editorial libros.editorial%type, price libros.precio%type)
is
begin
    insert into libros values (title,author,editorial,price);
end;
/

begin
    add_libros('&val1','&val2','&val3',&val4);
end;
/

select * from libros;